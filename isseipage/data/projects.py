def get_projects():
    return [
        {"id": 1, "image": "linebot.png", "title": "Daily Bot for AUD/JPY Excange Rates and English Vocabulary",
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
         "url": "https://github.com/IsseiToura/MyPortfolioWebsite"}
    ]