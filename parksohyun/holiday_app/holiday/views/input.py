# 입력 화면 불러들이기
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db

@app.route('/')
def show_home():
    # 프로젝트 폴더 내 'templates'라는 폴더를 기본 경로로 설정
    return render_template("input.html")