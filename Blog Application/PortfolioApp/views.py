import logging
from django.shortcuts import render
from math import ceil
from PortfolioApp.models import Portfolio
from BlogApp.exceptions.exception import ApplicationException

logger = logging.getLogger('blogapp-logger')
def render_home_page(request):
    try:
        portfolio_list = Portfolio.objects.all()
        # Creating range for DIV iteration in home.html page1
        portfolio_range = range(0,ceil(portfolio_list.count()/3))
        print(type(portfolio_range))
        print(portfolio_range)
    except Exception as e:
        logger.error(e)
        raise ApplicationException(e)
    return render(request, 'portfolio/home.html', context={'portfolio_list':portfolio_list, 'portfolio_range':portfolio_range})
