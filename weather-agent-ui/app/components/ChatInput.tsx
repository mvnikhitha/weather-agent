'use client'
import { useState } from 'react'

export default function ChatInput({ onSend }: { onSend: (query: string) => void }) {
  const [input, setInput] = useState("")

  const handleSend = () => {
    if (input.trim()) {
      onSend(input)
      setInput("")
    }
  }

  return (
    <div style={{ display: 'flex', gap: '10px', padding: '1rem' }}>
      <input
        type="text"
        value={input}
        placeholder="Ask a weather-related question..."
        onChange={(e) => setInput(e.target.value)}
        style={{ flexGrow: 1, padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
      />
      <button onClick={handleSend} style={{ padding: '10px 20px', backgroundColor: '#007BFF', color: 'white', border: 'none', borderRadius: '8px' }}>
        Send
      </button>
    </div>
  )
}