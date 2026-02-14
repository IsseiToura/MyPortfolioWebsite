/**
 * home.js - Home page (index.html) specific functionality
 * Handles Show More/Less functionality for Projects and Work Experience sections
 */

// ==================== Projects Section ====================
let currentlyShowing = 4;
let totalProjects = 0;
const projectsPerLoad = 4;

function showMoreProjects() {
  const projectItems = document.querySelectorAll('.project-item');
  const nextBatch = Math.min(currentlyShowing + projectsPerLoad, totalProjects);

  for (let i = currentlyShowing; i < nextBatch; i++) {
    if (projectItems[i]) {
      projectItems[i].style.display = 'block';
    }
  }

  currentlyShowing = nextBatch;

  // if all projects are displayed, change the button
  if (currentlyShowing >= totalProjects) {
    document.getElementById('showMoreBtn').style.display = 'none';
    document.getElementById('showLessBtn').style.display = 'inline-block';
  }
}

function showLessProjects() {
  const projectItems = document.querySelectorAll('.project-item');

  // hide the projects other than the first 4
  for (let i = 4; i < projectItems.length; i++) {
    projectItems[i].style.display = 'none';
  }

  currentlyShowing = 4;

  // reset the buttons
  document.getElementById('showMoreBtn').style.display = 'inline-block';
  document.getElementById('showLessBtn').style.display = 'none';

  // scroll to the project section
  document.getElementById('projects_anchor').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ==================== Work Experience Section ====================
let totalWorkExperiences = 0;

function showMoreWorkExperience() {
  const workItems = document.querySelectorAll('.work-experience-item');
  
  // Show all work experiences
  workItems.forEach(item => {
    item.style.display = 'block';
  });

  // Change buttons
  document.getElementById('showMoreWorkBtn').style.display = 'none';
  document.getElementById('showLessWorkBtn').style.display = 'inline-block';
}

function showLessWorkExperience() {
  const workItems = document.querySelectorAll('.work-experience-item');
  
  // Hide work experiences after the first 3
  workItems.forEach((item, index) => {
    if (index >= 3) {
      item.style.display = 'none';
    }
  });

  // Reset buttons
  document.getElementById('showMoreWorkBtn').style.display = 'inline-block';
  document.getElementById('showLessWorkBtn').style.display = 'none';
}

// ==================== Initialize ====================
document.addEventListener('DOMContentLoaded', function() {
  // Get total counts from data attributes
  const showMoreBtn = document.getElementById('showMoreBtn');
  const showMoreWorkBtn = document.getElementById('showMoreWorkBtn');
  
  if (showMoreBtn) {
    totalProjects = parseInt(showMoreBtn.getAttribute('data-total-projects')) || 0;
  }
  
  if (showMoreWorkBtn) {
    totalWorkExperiences = parseInt(showMoreWorkBtn.getAttribute('data-total-work-experiences')) || 0;
  }
});
