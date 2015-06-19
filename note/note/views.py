# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import TemplateView
from note import actions


class IndexView(TemplateView):
    template_name = '__start_page.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if 'session_id' in self.request.session:
            id_user = self.request.session['session_id']
            context['session'] = 'True'
            context['notes'] = actions.get_notes_user(id_user)
            context.update(actions.make_info(id_user))
        else:
            context['session'] = 'False'

        return context

    def post(self, request):
        # Add new tag
        if 'tag_name' in request.POST:
            status = actions.save_new_tag(
                request.POST['tag_name'], request.session['session_id'])
            return render_me(status, request)
        # Add new color
        elif 'color_name' in request.POST:
            status = save_color(request.POST['color_name'],
                                request.POST['hex'],
                                request.session['session_id'])
            return render_me(status, request)
        # Add new note
        elif 'subject' in request.POST:
            subj = actions.save_sub_note(request.session['session_id'],
                                         request.POST['subject'],
                                         request.POST['message'])
            colors = actions.save_color_note(request.POST['color'],
                                             request.POST['cat'])

            status = actions.save_new_note(request.POST.getlist('tag_ch'),
                                           request.FILES['file_load'],
                                           colors, subj)
            return render_me(status, request)
        # Add new category
        elif 'cat_name' in request.POST:
            status = actions.save_new_cat(request.POST['cat_name'],
                                          request.session['session_id'])
            return render_me(status, request)
        # Share
        elif 'share' in request.POST:
            return share_all(request)
        # Sign in user
        elif 'username' in request.POST:
            hash_code = actions.get_hash(
                request.POST['username'], request.POST['password'])
            key_answer = actions.get_user(hash_code)
            if key_answer != '-1':
                request.session['session_id'] = key_answer
                return render(request, 'success.html',)
            else:
                return render(request, 'warning.html',)


class SignUp(TemplateView):
    template_name = 'reg.html'

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        return context

    def post(self, request):
        rule = actions.get_hash(request.POST['username'],
                                request.POST['password'])

        user = actions.get_user(rule)

        if user != '-1':
            status = 403
        else:
            status = actions.save_new_user(request.POST['username'],
                                           request.POST['password'])

        return render_me(status, request)


class CatView(TemplateView):
    template_name = 'cat.html'

    def get_context_data(self, **kwargs):
        context = super(CatView, self).get_context_data(**kwargs)

        id_user = self.request.session['session_id']
        context['session'] = 'True'
        context['notes'] = actions.get_notes_cat(
            self.kwargs.get('pk'), id_user)
        context.update(actions.make_info(id_user))

        return context


class EditView(TemplateView):
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)

        id_user = self.request.session['session_id']
        context['session'] = 'True'
        context['notes'] = actions.get_notes_edit(
            self.kwargs.get('pk'))
        context.update(actions.make_info(id_user))

        return context

    def post(self, request, pk):

        subj = actions.save_sub_note(request.session['session_id'],
                                     request.POST['subject'],
                                     request.POST['message'])
        colors = actions.save_color_note(request.POST['color'],
                                         request.POST['cat'])

        status = actions.update_note(self.kwargs.get('pk'),
                                     request.POST.getlist('tag_ch'),
                                     request.FILES['file_load'],
                                     colors, subj)
        return render_me(status, request)


def share_all(request):
    if 'share_tag' in request.POST:
        status = actions.save_new_tag(request.POST['share_tag'],
                                      request.POST['share'])
        return render_me(status, request)
    elif 'share_cat' in request.POST:
        status = actions.save_new_cat(request.POST['share_cat'],
                                      request.POST['share'])
        return render_me(status, request)


def save_color(name, hex, id_user):
    status = actions.save_new_color(name, hex, id_user)
    return status


def down_file():
    return 'q'


def logout(request):
    del request.session['session_id']
    return render(request, 'success.html',)


def delete(request, id_note):
    status = actions.delete_note(id_note)
    return render_me(status, request)


def render_me(status, request):
    if status == 200 or status == 201 or status == 204:
        return render(request, 'success.html',)
    else:
        return render(request, 'warning.html',)
