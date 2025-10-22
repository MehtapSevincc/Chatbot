<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-r from-blue-400 to-green-400 ">
    
    <div class="w-full max-w-md bg-white rounded-xl shadow-md p-4">
              <h1 class="text-3xl font-bold  mb-4"> 
                 <span class="text-green-500">Hug</span><span class="text-blue-500">Bot </span>
                 <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" class="icon icon-tabler icons-tabler-filled icon-tabler-heart text-green-500"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6.979 3.074a6 6 0 0 1 4.988 1.425l.037 .033l.034 -.03a6 6 0 0 1 4.733 -1.44l.246 .036a6 6 0 0 1 3.364 10.008l-.18 .185l-.048 .041l-7.45 7.379a1 1 0 0 1 -1.313 .082l-.094 -.082l-7.493 -7.422a6 6 0 0 1 3.176 -10.215z" /></svg>
              </h1>
      <ChatBox :messages="messages" />
      <MessageInput v-model="userInput" @send="sendMessage" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChatBox from './components/ChatBox.vue'
import MessageInput from './components/MessageInput.vue'

const userInput = ref('')
const messages = ref([])

const sendMessage = async () => {
  if (!userInput.value.trim()) return

  messages.value.push({ role: 'user', text: userInput.value })
  const messageToSend = userInput.value
  userInput.value = ''

  try {
    const response = await fetch('http://localhost:5000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: messageToSend }),
    })
    const data = await response.json()
    messages.value.push({ role: 'bot', text: data.answer })
  } catch (error) {
    messages.value.push({ role: 'bot', text: 'Bağlantı hatası 😢' })
  }
}
</script>
