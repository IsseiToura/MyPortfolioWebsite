from flask import Blueprint, render_template, url_for
from isseipage.data.skills import get_skills
from isseipage.data.projects import get_projects

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    skills = get_skills()
    projects = get_projects()
    return render_template('index.html', skills=skills, projects=projects)

@main_bp.route('/projects/<int:project_id>')
def show_project_details(project_id):
    projects = get_projects()
    project = next((proj for proj in projects if proj["id"] == project_id), None)

    if project is None:
        return render_template('error.htmel'), 404

    return render_template('project_details.html', project=project)