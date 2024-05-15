import { useContext, useState } from 'react'
import { BackendContext } from '../Context'

function Message() {
  const BACKEND_BASE = useContext(BackendContext)
  const [message, setMessage] = useState('')

  async function handleClick() {
    const res = await fetch(BACKEND_BASE + '/message')
    const data = await res.json()

    setMessage(data.message)
  }

  return (
    <>
      <button onClick={handleClick}>Click Me</button>
      {message && <p>server says "{message}"</p>}
    </>
  )
}

export default Message
