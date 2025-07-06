# MyPortfolioWebsite

Welcome to MyPortfolioWebsite! This is a personal portfolio website designed to showcase my projects, skills, and experience in a modern and visually appealing way by using Python Flask.

## Features

- Responsive design for all devices
- Project showcase section
- About me section
- Contact form
- Easy customization
- AI-powered chat assistant (Issei GPT)

## Setup

### Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Copy `env.example` to `.env`
   - Add your API keys to `.env`:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     SERP_API_KEY=your_serp_api_key_here
     ```
5. Run the application:
   ```bash
   python app.py
   ```

### Deployment on Render

1. Push your code to GitHub
2. Connect your repository to Render
3. Set environment variables in Render dashboard:
   - `OPENAI_API_KEY`
   - `SERP_API_KEY`
4. Deploy using the `render.yaml` configuration

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for GPT functionality
- `SERP_API_KEY`: Your SerpAPI key for web search functionality
