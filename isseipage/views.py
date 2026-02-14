from flask import Blueprint, render_template
from isseipage.data.skills import get_skills
from isseipage.data.projects import get_projects
from isseipage.data.work_experiences import get_work_experiences, get_education

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    skills = get_skills()
    projects = get_projects()
    work_experiences = get_work_experiences()
    education = get_education()
    return render_template('index.html', skills=skills, projects=projects, work_experiences=work_experiences, education=education)

@main_bp.route('/projects/<int:project_id>')
def show_project_details(project_id):
    projects = get_projects()
    project = next((proj for proj in projects if proj["id"] == project_id), None)

    if project is None:
        return render_template('error.htmel'), 404

    return render_template('project_details.html', project=project)

@main_bp.route('/issei_gpt')
def issei_gpt():
    return render_template('issei_gpt.html')