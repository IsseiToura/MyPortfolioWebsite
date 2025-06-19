def get_projects():
    projects = [
        {"id": 1, "image": "linebot.png", "title": "Daily Bot for AUD/JPY Rate and English Vocabulary",
         "description": "1. Developed a bot that retrieves AUD/JPY exchange rates and English vocabulary words daily from APIs and stores in a databese." \
                        "\n\n2. The bot sends this information to a messaging app automatically once a day." \
                        "\n\n3. Built a vocabulary learning app that displays a list of vocabulary words stored in a database. Users can also add their own words they want to learn."\
                        "\n\n* This was a collaborative project, and I was responsible for implementing the vocabulary-related features", 
         "environment": " - Language: TypeScript\n - DB: MongoDB, Docker\n - Others: Next.js, OpenAI API",
         "url": "https://github.com/IsseiToura/AUDJPNNotification"},

        {"id": 2, "image": "boardgame.png", "title": "Board Game (Gomoku & Noktakto)",
         "description": "1. Developed the mechanics for two games: Gomoku and Noktakto." \
                        "\n\n2. Implemented two game modes: Human vs. Human and Human vs. Computer Player."\
                        "\n\n3. Designed with object-oriented principles, enabling easy implementation of other one-on-one board games. The project incorporates design patterns such as the Factory Method Pattern and Template Method Pattern.", 
         "environment": " - Language: C#\n - Others: .NET",
         "url": "https://github.com/IsseiToura/BoardGame"},

         {"id": 3, "image": "myportfolio.png", "title": "My Portfolio Website",
         "description": "1. Created a personal portfolio website to showcase my work as a software developer, using Python Flask." \
                        "\n\n2. Utilized Bootstrap to ensure responsive design, making the website compatible with various screen sizes, including PCs, tablets, and smartphones.",
         "environment": " - Language: Python, HTML, CSS\n - Others: Python Flask, BootStrap",
         "url": "https://github.com/IsseiToura/MyPortfolioWebsite"},

         {"id": 4, "image": "VocabMaster.png", "title": "Vocabulary Master",
         "description": "1. Uses the OpenAI API to automatically generate English words tailored to your selected IELTS level, including pronunciation, Japanese translations, and example sentences." \
                        "\n\n2. Lets you build your own vocabulary list by adding only the words you want to learn." \
                        "\n\n3. Includes a flashcard practice feature that shows 10 random words from your list so you can review them interactively." \
                        "\n\n4. Tracks your practice history, showing which words you got right or wrong to help you focus on improvement.",
         "environment": " - Language: JavaScript\n - DB: MongoDB\n - Others: Node.js, OpenAI API",
         "url": "https://www.linkedin.com/posts/issei-toura-1502851a1_ielts-englishlearning-reactjs-activity-7334758600831025152-maV_?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC80UowB-h4CtQwXDHw9lxwFfPUT2oHqn_Y"},

         {"id": 5, "image": "Forensic.png", "title": "Forensic Data Visualizer",
         "description": "1. Implemented automated PDF parsing and information extraction." \
                        "\n\n2. Cross-document entity matching using keys such as ACNs and full names." \
                        "\n\n3. Auto-generated relationship diagrams, and structured data export to Excel for further analysis." \
                        "\n\n4. This was a collaborative project, and my role was project manager and developer.",
         "environment": " - Language: Python and TypeScript\n - Others: Python Flask, PDFPlumber, React",
         "url": "https://www.linkedin.com/posts/issei-toura-1502851a1_as-part-of-my-university-curriculum-i-had-activity-7339480483979776002-QgEZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC80UowB-h4CtQwXDHw9lxwFfPUT2oHqn_Y"}
    ]
    
    # IDを逆順（降順）でソートして返す
    return sorted(projects, key=lambda x: x["id"], reverse=True)