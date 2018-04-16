from django.shortcuts import render
from .models import StudentDetails,TeacherDetails
from django.contrib.auth.models import User,Group
from django.template import RequestContext

import re

from django.db.models import Q

# Create your views here.
def index(request):
	user = request.user
	if user.groups.filter(name='teacher').exists():
		obj = TeacherDetails.objects.filter(teacher_user = user)
	elif user.groups.filter(name='student').exists():
		obj = StudentDetails.objects.filter(student_user = user)
	return render(request,"core/index.html",{"test_data":"Hello World","flag_data":"Hello Again","title":"index"})


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['subject', 'phone',])

        found_entries = TeacherDetails.objects.filter(entry_query)

    return render('core/search_result.html',
                          { 'query_string': query_string, 'found_entries': found_entries })