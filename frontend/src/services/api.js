import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const api = {
  // Health
  checkHealth: () => axios.get('http://localhost:8000/health'),

  // Resumes
  uploadResume: (formData) => apiClient.post('/resume/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  }),

  // Jobs
  getSavedJobs: () => apiClient.get('/jobs'),
  saveJob: (jobData) => apiClient.post('/jobs', jobData),

  // Analysis
  runAnalysis: (payload) => apiClient.post('/analyze', payload),
  getAnalyses: () => apiClient.get('/analyses'),
  getAnalysisById: (id) => apiClient.get(`/analyses/${id}`),
  deleteAnalysis: (id) => apiClient.delete(`/analyses/${id}`),

  // Skills
  getSkillsCatalog: () => apiClient.get('/skills'),
  addCustomSkill: (skillData) => apiClient.post('/skills', skillData),

  // Learning Checklist
  getChecklist: (analysisId) => apiClient.get(`/learning-checklist/${analysisId}`),
  updateChecklistItemStatus: (itemId, status) => apiClient.patch(`/learning-checklist/${itemId}`, { status }),

  // Evaluation
  getModelEvaluation: () => apiClient.get('/evaluation'),
};
