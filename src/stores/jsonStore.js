import { defineStore } from 'pinia'

export const useJsonStore = defineStore('jsonStore', {
  state: () => ({
    uploadedData: null,
    fileName: ''
  }),

  actions: {
    setJsonData(data, name) {
      this.uploadedData = data;
      this.fileName = name;
    },
    clearData() {
      this.uploadedData = null;
      this.fileName = '';
    }
  }
})