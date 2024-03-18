# Главные импорты django
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
# Доп библиотеки
import random
import string
import hashlib
import base64
import time
import logging
import uuid
import sys
import json
import requests

def main(request):  # Главная страница
    return render(request, 'main/main.html')

def custom_logout(request):  # Самописный выход
    logout(request)
    return HttpResponseRedirect('https://heylon.ru')