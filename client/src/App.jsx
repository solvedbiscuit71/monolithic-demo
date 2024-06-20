import { useState } from "react"

function App() {
  const [message, setMessage] = useState('');
  
  async function handleRequest() {
    const res = await fetch(import.meta.env.VITE_API + '/message');
    const data = await res.json();
    setMessage(data.message);
  }

  return (
    <>
      <button onClick={handleRequest}>Click Me</button>
      <p>Server response: {message}</p>
    </>
  )
}

export default App
