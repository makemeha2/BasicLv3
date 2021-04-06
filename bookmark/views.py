from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import path
from bookmark.models import Bookmark

class BookmarkLV(ListView) : 
    model = Bookmark

class BookmarkDV(DetailView) :
    model = Bookmark