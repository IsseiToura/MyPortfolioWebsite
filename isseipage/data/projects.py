"""
Projects data
"""

def get_projects():
    """Get list of projects sorted by ID in descending order"""
    return sorted(projects, key=lambda x: x['id'], reverse=True)

projects = [
    {
        'id': 1,
        'image': 'linebot.png',
        'title': 'Daily Bot for AUD/JPY Rate and English Vocabulary',
        'features': [
            'Developed a bot that retrieves AUD/JPY exchange rates and English vocabulary words daily from APIs and stores in a database.',
            'The bot sends this information to a messaging app automatically once a day.',
            'Built a vocabulary learning app that displays a list of vocabulary words stored in a database. Users can also add their own words they want to learn.',
            '* This was a collaborative project, and I was responsible for implementing the vocabulary-related features'
        ],
        'tech_stack': {
            'language': 'TypeScript',
            'others': 'Next.js, OpenAI API, MongoDB, Docker'
        },
        'url': 'https://github.com/IsseiToura/AUDJPNNotification'
    },
    {
        'id': 2,
        'image': 'boardgame.png',
        'title': 'Board Game (Gomoku & Noktakto)',
        'features': [
            'Developed the mechanics for two games: Gomoku and Noktakto.',
            'Implemented two game modes: Human vs. Human and Human vs. Computer Player.',
            'Designed with object-oriented principles, enabling easy implementation of other one-on-one board games. The project incorporates design patterns such as the Factory Method Pattern and Template Method Pattern.'
        ],
        'tech_stack': {
            'language': 'C#',
            'others': '.NET'
        },
        'url': 'https://github.com/IsseiToura/BoardGame'
    },
    {
        'id': 3,
        'image': 'myportfolio.png',
        'title': 'My Portfolio Website',
        'features': [
            'Created a personal portfolio website to showcase my work as a software developer, using Python Flask.',
            'Utilized Bootstrap to ensure responsive design, making the website compatible with various screen sizes, including PCs, tablets, and smartphones.'
        ],
        'tech_stack': {
            'language': 'Python, HTML, CSS',
            'others': 'Python Flask, Bootstrap'
        },
        'url': 'https://github.com/IsseiToura/MyPortfolioWebsite'
    },
    {
        'id': 4,
        'image': 'VocabMaster.png',
        'title': 'Vocabulary Master',
        'features': [
            'Uses the OpenAI API to automatically generate English words tailored to your selected IELTS level, including pronunciation, Japanese translations, and example sentences.',
            'Lets you build your own vocabulary list by adding only the words you want to learn.',
            'Includes a flashcard practice feature that shows 10 random words from your list so you can review them interactively.',
            'Tracks your practice history, showing which words you got right or wrong to help you focus on improvement.'
        ],
        'tech_stack': {
            'language': 'JavaScript',
            'others': 'Node.js, OpenAI API, MongoDB'
        },
        'url': 'https://www.linkedin.com/posts/issei-toura-1502851a1_ielts-englishlearning-reactjs-activity-7334758600831025152-maV_?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC80UowB-h4CtQwXDHw9lxwFfPUT2oHqn_Y'
    },
    {
        'id': 5,
        'image': 'Forensic.png',
        'title': 'Forensic Data Visualizer',
        'features': [
            'Implemented automated PDF parsing and information extraction.',
            'Cross-document entity matching using keys such as ACNs and full names.',
            'Auto-generated relationship diagrams, and structured data export to Excel for further analysis.',
            '* This was a collaborative project, and my role was project manager and developer.'
        ],
        'tech_stack': {
            'language': 'Python, TypeScript',
            'others': 'Python Flask, PDFPlumber, React'
        },
        'url': 'https://www.linkedin.com/posts/issei-toura-1502851a1_as-part-of-my-university-curriculum-i-had-activity-7339480483979776002-QgEZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC80UowB-h4CtQwXDHw9lxwFfPUT2oHqn_Y'
    },
    {
        'id': 6,
        'image': 'video-transcriber-ai.png',
        'title': 'Video Transcriber AI',
        'features': [
            'Creates transcripts from long videos (audio) and automatically generates summaries of the content.',
            {
                'text': 'Built with event-driven architecture to seamlessly process the entire workflow:',
                'subitems': [
                    'User uploads video → stored in S3',
                    'Lambda function sends message to SQS → triggers automatic transcription and summarization',
                    'ECS scales out when queue grows, scales in when only one message remains'
                ]
            },
            'Developed as a cloud-native application using AWS. Main AWS services used: CloudFront, Lambda, ECS, SQS, DynamoDB, and S3.'
        ],
        'tech_stack': {
            'language': 'Python, TypeScript',
            'others': 'AWS (ECS, CloudFront, Lambda, DynamoDB, etc.), OpenAI API'
        },
        'url': 'https://www.linkedin.com/posts/issei-toura-1502851a1_cloudcomputing-aws-serverless-activity-7395966301892112384-_Kvp?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC80UowB-h4CtQwXDHw9lxwFfPUT2oHqn_Y'
    }
]
