// app/layout.tsx
'use client'; // This makes the component client-side, where hooks are available

import './globals.css';
import { ReactNode, useState, useEffect } from 'react';

// Function to determine the background class based on weather or time
const getWeatherBackground = (weather: string) => {
  switch (weather) {
    case 'clear':
      return 'bg-clear';
    case 'rainy':
      return 'bg-rainy';
    case 'snow':
      return 'bg-snow';
    case 'night':
      return 'bg-night';
    default:
      return 'bg-default';
  }
};

export default function RootLayout({ children }: { children: ReactNode }) {
  const [currentWeather, setCurrentWeather] = useState<string>('clear'); // Initial background state

  useEffect(() => {
    const weatherTypes = ['clear', 'rainy', 'snow', 'night']; // Possible background states

    // Function to randomly change background
    const changeWeather = () => {
      const randomWeather = weatherTypes[Math.floor(Math.random() * weatherTypes.length)];
      setCurrentWeather(randomWeather); // Update background every time
    };

    const intervalId = setInterval(changeWeather, 5000); // Change every 5 seconds

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array to run effect once on mount

  const weatherBgClass = getWeatherBackground(currentWeather);

  return (
    <html lang="en">
      <body className={`min-h-screen ${weatherBgClass}`}>
        {children}
      </body>
    </html>
  );
}
