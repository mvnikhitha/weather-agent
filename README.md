# 🌦️ Weather & Activity Planning Chatbot

This repository contains an AI-powered chatbot designed to provide real-time weather information 🌤️ and help users plan activities based on the weather 🌳. The chatbot integrates with APIs for accurate weather data 🌍, includes persistent memory using a vector database 🧠, and is built with a dynamic, responsive frontend using **Next.js**.

## 📌 Overview

The **Weather & Activity Planning Chatbot** uses real-time weather data to suggest activities based on current conditions 🌦️. It features persistent memory to provide personalized recommendations and integrates with APIs like OpenWeather for weather updates. The frontend includes dynamic weather-based backgrounds 🌈, smooth transitions 💨, and a user-friendly chat interface.

## 🛠 Technologies Used
- **Frontend**: Next.js (React) 💻
- **Backend**: Gemini (LLM), Agno or LangChain ⚙️
- **Database**: Pinecone / Supabase (Vector DB for persistent memory) 🗃️
- **Weather API**: OpenWeather, or any other weather data provider 🌥️
- **Hosting**: Vercel / Netlify (for frontend) 🌐

## 🚀 Features
- **Real-time Weather Data**: Fetches weather information using external APIs (e.g., OpenWeather API) 🌦️.
- **Persistent Memory**: The chatbot retains memory across conversations using a vector database (Pinecone or Supabase) 🧠.
- **Activity Planning**: Suggests activities based on the weather forecast 🏃‍♀️🎨.
- **Responsive UI**: Frontend built with Next.js featuring dynamic weather-based backgrounds 🌈 and animated elements 🎞️.
- **Smooth Transitions**: Seamless UI transitions with animated weather location displays, chat bubbles, and background animations 💨.

## 📂 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mvnikhitha/weather-agent.git
cd weather-agent
```
### 2️⃣ Install Dependencies
```bash
npm install
```
### 3️⃣ Set Up Environment Variables
Create a .env file in the root directory and add the following:
```bash
env
Copy
Edit
WEATHER_API_KEY=your_weather_api_key
VECTOR_DB_API_KEY=your_pinecone_or_supabase_api_key (optional)
```
### 4️⃣ Run the Development Server
```bash
npm run dev
```
### 5️⃣ Navigate to the Chatbot
Open your browser and go to http://localhost:3000 🌍 to see the chatbot in action.

## 💬 Usage

- **Chatbot**: The chatbot will provide real-time weather updates 🌤️ and suggest activities based on the weather 🌦️.
- **Persistent Memory**: The chatbot will remember previous interactions for a more personalized experience 🧠.
- **Activity Suggestions**: After retrieving the weather forecast, the chatbot will suggest outdoor activities 🏞️, workouts 🏋️‍♀️, or indoor alternatives 🎮 based on the current conditions.

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, submit issues, and create pull requests. Here's how you can contribute:

1. Fork the repository 🍴  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
    ```
3. Make your changes ✨

4. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
5. Push to the branch:

```bash
git push origin feature-branch
```
6. Open a pull request 📝

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details 📜.

**Author**: [M V Nikhitha]

