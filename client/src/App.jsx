import { useState } from "react"

function App() {
  const [message, setMessage] = useState('');
  const [count, setCount] = useState('');
  
  async function handleRequest() {
    const res = await fetch(import.meta.env.VITE_API + '/message');
    const data = await res.json();
    setMessage(data.message);
    setCount(data.count);
  }

  return (
    <>
      <p>
        Send a request to server: <button onClick={handleRequest}>Click Me</button>
      </p>

      <fieldset>
        <h2>Server response:</h2>
        <p>message: "{message}"</p>
        <p>count: {count}</p>
      </fieldset>
    </>
  )
}

export default App
