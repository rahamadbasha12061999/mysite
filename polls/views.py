# Django Imports
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import (
    render,
    get_object_or_404
)

# Local App Imports
from .models import (
    Question,
    Choice,
    Email
)
from .forms import (
    QuestionForm,
    EmailForm
)


def page(request):
    return HttpResponse("Hello world")


def info(request):
    return HttpResponse("How are you?")


def calculate(request, principle, months, rate_of_interest):
    print(principle, months, rate_of_interest)
    total = principle * (1 + (float(rate_of_interest) * months / 100))
    return HttpResponse(f"Ur amount, principle: {principle}, months: {months}, rate_of_interest: {rate_of_interest}"
                        f"\nTotal={total}")


def simple_interset(request, principle, months, rate_of_interest):
    """
    :param request:
    :param principle:
    :param months:
    :param rate_of_interest:
    :return:
    """
    print(principle, months, rate_of_interest)
    total = principle * (1 + (float(rate_of_interest) * months / 100))
    data = {
        "name": "surESH KUMAr",
        "aadhaar": "123456789012",
        "principle": principle,
        "months": months,
        "rate_of_interest": rate_of_interest,
        "total": total
    }
    return render(request, template_name="simple-interest.html", context=data)


def html_render(request):
    return render(request, "polls/mypage.html")


def temp_data(request):
    data = {
        "my_list": ["suresh", "kumar", ("Python", "Djnago", "Sql"), "bangalore"],
        "name": "Hcl india pvt ltd",
        "my_dict": {
            "status": "active",
            "fname": "suresh",
            "lname": "kumar",
            "location": "Bangalore",
            "skills": ["Python", "Djnago", "Sql"]
        },
        "salary": (100000, 120000, 150000, 105000, 160000, 145000)
    }
    return render(request, "my_page.html",
                  context={"mydata": data})


def index(request):
    questions = Question.objects.all()
    return render(request, template_name="polls/index.html",
                  context={"que": questions})


def choices(request, question_id):
    question = Question.objects.get(id=question_id)
    cho = Choice.objects.filter(question=question)
    return render(request, template_name="polls/choices.html",
                  context={"question": question, "choices": cho})


def create_question(request):
    if request.method == "POST":
        question = Question.objects.create(
            question_text=request.POST["question"],
            pub_date=timezone.now()
        )
        return HttpResponseRedirect(reverse("polls:questions", args=tuple()))
    else:
        return render(request, template_name="polls/create_question.html")


def create_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        choice = Choice.objects.create(
            question=question,
            choice_text=request.POST["choice"],
            votes=request.POST["votes"]
        )
        return HttpResponseRedirect(reverse("polls:choices", args=(question.pk,)))
    else:
        return render(
            request,
            template_name="polls/create_choice.html",
            context={"question": question})


def question_djforms(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(
                question_text=form.cleaned_data.get("question_text"),
                pub_date=timezone.now()
            )
            return HttpResponseRedirect(reverse("polls:questions", args=tuple()))
        else:
            return render(request, template_name="polls/df_create_question.html", context={"form": form})
    else:
        form = QuestionForm()
        return render(request, template_name="polls/df_create_question.html", context={"form": form})


def emails(request):
    emails = Email.objects.all()
    return render(request, template_name="email/emails.html", context={"emails": emails})


def create_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("polls:all-emails", args=tuple()))
        else:
            return render(request, template_name="email/create.html", context={"form": form})
    else:
        form = EmailForm()
        return render(request, template_name="email/create.html", context={"form": form})


def email_detail(request, pk):
    email = get_object_or_404(Email, pk=pk)
    return render(request, template_name="email/detail.html", context={"email": email})


def edit_email(request, pk):
    email = get_object_or_404(Email, pk=pk)
    if request.method == "POST":
        email.from_email = request.POST["from"]
        email.to_email = request.POST["to"]
        email.subject = request.POST["subject"]
        email.body = request.POST["body"]
        email.save()
        return HttpResponseRedirect(reverse("polls:detail-email", args=(email.pk, )))

    else:
        return render(request, template_name="email/edit_email.html", context={"email": email})

def edit_email_dj(request, pk):
    email = get_object_or_404(Email, pk=pk)
    if request.method == "POST":
        form = EmailForm(request.POST, instance=email)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("polls:all-emails", args=tuple()))
        else:
            return render(request, template_name="email/edit-dj.html", context={"form": form})
    else:
        form = EmailForm(instance=email)
        return render(request, template_name="email/edit-dj.html", context={"form": form})
