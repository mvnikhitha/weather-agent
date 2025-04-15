'use client';

import React, { useState, useRef, useEffect } from 'react';
import './globals.css';

type Message = {
  sender: 'user' | 'bot';
  text: string;
};

export default function ChatPage() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  const handleSend = async () => {
    const trimmedInput = input.trim();
    if (!trimmedInput || loading) return;

    const userMsg: Message = { sender: 'user', text: trimmedInput };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: '123', message: trimmedInput }),
      });

      if (!res.ok) throw new Error('API error');

      const data = await res.json();
      const botText = data.response || data.error || 'Unexpected response';
      const botMsg: Message = { sender: 'bot', text: botText };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      const botMsg: Message = { sender: 'bot', text: 'Something went wrong. Please try again.' };
      setMessages((prev) => [...prev, botMsg]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <main className="flex flex-col h-screen p-4 bg-gradient-to-br from-blue-100 to-blue-300">
      <h1 className="text-4xl font-bold text-center text-blue-700 mb-6 animate-fadeSlide">
        ⛅ Weather Agent 😎
      </h1>

      <div className="flex-1 overflow-y-auto px-4 space-y-4 chat-container">
        {messages.map((msg, index) => (
          <div key={index} className="flex justify-between items-start">
            <div
              className={`chat-message ${msg.sender === 'user' ? 'user-bubble' : 'bot-bubble'}`}
            >
              {msg.sender === 'user' ? '😎' : '☁️'} {msg.text}
            </div>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      {/* Final Clean Input Area */}
      <div className="input-area flex gap-2 p-4 mt-4 bg-white rounded-xl shadow-md">
        <input
          type="text"
          className="flex-1 px-4 py-2 bg-white text-black border border-blue-400 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition placeholder:text-gray-500 disabled:opacity-50"
          value={input}
          placeholder={loading ? 'Waiting for response...' : 'Ask me anything...'}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          disabled={loading}
        />
        <button
          className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-2xl shadow-md transition disabled:opacity-50"
          onClick={handleSend}
          disabled={loading}
        >
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </main>
  );
}
