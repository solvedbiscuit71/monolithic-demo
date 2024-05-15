import { BackendContext } from './Context'
import Message from './components/Message'

function App() {
  return (
    <BackendContext.Provider value={import.meta.env.DEV ? 'http://127.0.0.1:5000/api' : '/api'}>
      <Message/>
    </BackendContext.Provider>
  )
}

export default App
