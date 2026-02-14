"""
Work Experience and Education data
"""

def get_work_experiences():
    """Get list of work experiences"""
    return work_experiences

def get_education():
    """Get list of education"""
    return education

work_experiences = [
    {
        'id': 1,
        'company': 'Recruit Holdings Co., Ltd.',
        'positions': [  # Multiple positions at the same company (oldest first)
            {
                'role': 'Enterprise Sales',
                'start_date': '04/2019',
                'end_date': '03/2022',
                'responsibilities': [
                    'Served as a major sales representative for mid-career recruitment advertising.'
                ]
            },
            {
                'role': 'Sales Leader',
                'start_date': '04/2022',
                'end_date': '09/2023',
                'responsibilities': [
                    'Worked as a sales leader for inside sales of cashless payment terminals.'
                ]
            }
        ]
    },
    {
        'id': 2,
        'company': 'Anycloud Co., Ltd.',
        'role': 'Frontend Developer',
        'start_date': '03/2025',
        'end_date': '07/2025',
        'responsibilities': [
            'Developed the frontend of an inventory management application, utilizing a tech stack including TypeScript, React, and Next.js.'
        ]
    },
    {
        'id': 3,
        'company': 'Cumming Technologies Pty Ltd',
        'role': 'Software Developer',
        'start_date': '07/2025',
        'end_date': '11/2025',
        'responsibilities': [
            'Built a backend system with data pipelines using Java, Guava, JDBI, and PostgreSQL to collect and process global horse racing data for modeling purposes.',
            'Developed a frontend application using Vue.js to process and monitor real-time horse racing data.'
        ]
    },
    {
        'id': 5,
        'company': 'Semurg Enterprise Pty Ltd',
        'role': 'Software Developer',
        'start_date': '12/2025',
        'end_date': 'Present',
        'responsibilities': [
            'Developed an application that protects confidential information (e.g., PII, API keys) by implementing a secure tokenisation system.',
            'Built a translation application leveraging local and open-source LLM models to process multimodal data.',
            'Developed a real-time client application using WebSockets and a publish-subscribe architecture.'
        ]
    }
]

education = [
    {
        'id': 1,
        'institution': 'The University of Tokyo',
        'degree': 'Bachelor of Psychology',
        'start_date': '04/2015',
        'end_date': '03/2019'
    },
    {
        'id': 2,
        'institution': 'Queensland University of Technology (QUT)',
        'degree': 'Master of Computer Science',
        'start_date': '02/2024',
        'end_date': '12/2025'
    }
]
