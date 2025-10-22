<template>
  <div class="h-96 overflow-y-auto border p-2 mb-4">
    <div v-for="(msg, index) in messages" :key="index" class="mb-2">
      <div v-if="msg.role === 'user'" class="text-right">
        <span
          class="bg-sky-400 text-white px-3 py-2 rounded-lg inline-block max-w-xs break-words"
        >{{ msg.text }}</span>
      </div>
      <div v-else class="text-left">
        <span
          class="bg-gray-200 text-black px-3 py-2 rounded-lg inline-block max-w-xs break-words"
        >{{ msg.text }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  messages: {
    type: Array,
    required: true,
  },
})
</script>
