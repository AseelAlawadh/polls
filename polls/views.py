from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic

# def index(request):
#     # return HttpResponse("Hello world, you are at the polls index ")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ','.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # tamplate = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list, }
#     # return HttpResponse(tamplate.render(context, request))
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question':question})
#     # # return HttpResponse('you are looking at question %s' % question_id)
#     question = get_list_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})
#
# def results(request, question_id):
#     # response = 'you are looking at the results of question %s'
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html',{'question':question})
#
# def vote(request, question_id):
#     # return HttpResponse('you are looking on question %s' % question_id
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {'question':question, 'error_message': "you didn't select a choice",})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

"""" Use generic views """
class IndexView(generic.ListView):
    tamplate_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """" return the last 5 published questios """
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    tamplate_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    tamplate_name = 'polls/results.html'

def vote(request, question_id):
    # return HttpResponse('you are looking on question %s' % question_id
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message': "you didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
