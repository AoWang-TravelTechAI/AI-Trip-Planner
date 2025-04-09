# 🧭 AI Trip Planner

An AI-powered travel assistant that generates personalized travel itineraries based on user-input destinations and trip length. Built with a clean web interface and powered by Groq’s large language model API, this app is a core demonstration of applying AI in the tourism domain.

---

## 🌐 Overview

This project is part of my career transition journey from tourism management to computer science. It showcases my ability to combine AI and real-world travel data to build intelligent tools that enhance trip planning and personalization.

---

## ⚙️ Features

- **LLM-Generated Itineraries:** Uses Groq API to generate detailed multi-day itineraries (e.g., attractions, food, timing, activities).
- **Clean Flask Interface:** Users can input destinations and get instant day-by-day plans.
- **Google Maps Integration:** Retrieves real-time top 5 attractions via Google Maps API.
- **Modular Backend:** Easy to upgrade from Groq to OpenAI, Claude, or other models.

---

## 🧠 Technologies

| Layer        | Tech Stack                            |
|--------------|----------------------------------------|
| Frontend     | HTML, JavaScript                       |
| Backend      | Python, Flask                          |
| AI API       | Groq (Mixtral model)                   |
| External API | Google Maps Places API                 |
| Deployment   | Localhost (Docker/Render in progress)  |

---

## 🔄 How It Works

1. User enters a destination and number of days.
2. Flask backend sends prompt to Groq's Mixtral LLM via API.
3. Model returns a full itinerary.
4. UI displays day-by-day plan and top attractions.

---

## 🧪 Sample Output

> **Destination:** New York  
>  
> **Day 1:**  
> - Times Square  
> - Empire State Building  
> - Brooklyn Bridge  
> - Italian Dinner at Carbone  
>  
> **Day 2:**  
> - Central Park  
> - The Met Museum  
> - Guggenheim  
>  
> **Day 3:**  
> - One World Trade Center  
> - Little Italy  
> - Sunset Hudson Cruise

---

## 🚀 Future Enhancements

- [ ] Full deployment via Render or Docker  
- [ ] GPT-4 Vision support (upload travel photos/maps)  
- [ ] User login & itinerary history  
- [ ] Vector search for personalized recommendations  
- [ ] Preference-based trip generation (e.g., foodie, art-lover, nature)

---

## 👨‍💻 Author

**Ao Wang**  
🎓 M.S. in Computer Science @ Stevens Institute of Technology  
🎯 Career Goal: AI + Tourism | TravelTech Innovator  
🔗 [GitHub](https://github.com/AoWang-TravelTechAI) | [LinkedIn](https://linkedin.com/in/yourprofile)  

---

> This project reflects my passion and direction to break into the Travel Tech field with a blend of AI, design, and domain expertise.

