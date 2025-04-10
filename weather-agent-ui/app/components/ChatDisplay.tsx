export default function ChatDisplay({ response }: { response: string }) {
    return (
      <div style={{ padding: '1rem', margin: '0 1rem', backgroundColor: '#f5f5f5', borderRadius: '10px', minHeight: '100px' }}>
        {response || "Agent response will appear here..."}
      </div>
    )
  }