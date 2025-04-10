"use client";
import { useState } from "react";

export default function Home() {
  const [location, setLocation] = useState("");
  const [weather, setWeather] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const fetchWeather = async () => {
    if (!location) return;
    setLoading(true);
    try {
      const res = await fetch(`http://localhost:8000/weather?location=${location}`);
      const data = await res.json();
      setWeather(data);
    } catch (err) {
      console.error("Error fetching weather:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-background text-foreground px-4">
      <h1 className="text-3xl font-bold mb-4">🌦️ Weather Agent</h1>
      <div className="flex gap-2 mb-6 w-full max-w-md">
        <input
          type="text"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Enter a location"
          className="flex-1 p-2 border rounded text-black"
        />
        <button
          onClick={fetchWeather}
          className="bg-black text-white px-4 py-2 rounded hover:bg-gray-800"
        >
          {loading ? "Loading..." : "Search"}
        </button>
      </div>

      {weather && (
        <div className="bg-white text-black p-4 rounded shadow max-w-md w-full">
          <h2 className="text-xl font-semibold mb-2">{weather.location}</h2>
          <p>Temperature: {weather.temperature}°C</p>
          <p>Condition: {weather.condition}</p>
        </div>
      )}
    </div>
  );
}
