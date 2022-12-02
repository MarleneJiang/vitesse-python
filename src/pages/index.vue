<script setup lang="ts">
defineOptions({
  name: 'IndexPage',
})
const user = useUserStore()
const name = $ref(user.savedName)

const router = useRouter()
const go = () => {
  if (name)
    router.push(`/hi/${encodeURIComponent(name)}`)
}

const pythonName = ref('')
const getOwner = async () => {
  pythonName.value = await window.pywebview.api.getOwner() // 前端调用Python暴露的方法
}
getOwner()

const pythonData = ref('')

const getPythonData = () => {
  pythonData.value = 'Python调用了此方法'
}

window.getPythonData = getPythonData // 暴露方法给Python调用

const { t } = useI18n()
</script>

<template>
  <div>
    <div text-4xl>
      <div i-carbon-campsite inline-block />
    </div>
    <p>
      <a rel="noreferrer" href="https://github.com/antfu/vitesse" target="_blank">
        Vitesse
      </a>
    </p>
    <p>
      <em text-sm opacity-75>{{ t('intro.desc') }}</em>
    </p>

    <div py-4 />
    <div>{{ pythonData }}</div>
    <div py-4 />

    <Input
      v-model="name"
      placeholder="What's your name?"
      autocomplete="false"
      :value="pythonName"
      @keydown.enter="go"
    />
    <label class="hidden" for="input">{{ t('intro.whats-your-name') }}</label>

    <div>
      <button
        btn m-3 text-sm
        :disabled="!name"
        @click="go"
      >
        {{ t('button.go') }}
      </button>
    </div>
  </div>
</template>

<route lang="yaml">
meta:
  layout: home
</route>
