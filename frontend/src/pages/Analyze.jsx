import React, { useState } from 'react';
import { 
  Upload, 
  FileText, 
  Briefcase, 
  Building2, 
  FileSearch, 
  Sparkles, 
  CheckCircle2, 
  XCircle, 
  PlusCircle, 
  AlertCircle,
  RefreshCw,
  BookOpen
} from 'lucide-react';
import { api } from '../services/api';
import SimilarityGauge from '../components/SimilarityGauge';
import SkillBadge from '../components/SkillBadge';
import ChecklistTable from '../components/ChecklistTable';

export default function Analyze() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadedResumeId, setUploadedResumeId] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [uploading, setUploading] = useState(false);

  const [jobTitle, setJobTitle] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [jobText, setJobText] = useState('');
  const [resumeText, setResumeText] = useState('');

  const [analysisResult, setAnalysisResult] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  const loadSampleJobText = () => {
    setJobTitle('Senior Full-Stack Engineer');
    setCompanyName('CloudScale Systems');
    setJobText(
      `Job Title: Senior Full-Stack Engineer\nCompany: CloudScale Systems\n\nAbout the Role:\nWe are looking for a passionate Full-Stack Engineer to join our core product development team. You will build high-throughput web applications, design REST APIs, and deploy cloud-native microservices.\n\nKey Responsibilities:\n- Develop scalable front-end components using React, TypeScript, and Tailwind CSS.\n- Architect high-performance backend microservices with Node.js, Express.js, or FastAPI.\n- Manage relational and NoSQL databases, specifically PostgreSQL and Redis.\n- Implement containerization with Docker and orchestration via Kubernetes.\n- Drive CI/CD pipelines using GitHub Actions or Jenkins on AWS cloud infrastructure.\n- Collaborate in an Agile/Scrum team using Git for version control.\n\nRequired Qualifications & Technical Skills:\n- Programming Languages: JavaScript, TypeScript, Python, SQL\n- Frameworks: React, Node.js, FastAPI, Express.js\n- Cloud & Infrastructure: AWS, Docker, Kubernetes, CI/CD, Linux\n- Databases: PostgreSQL, Redis\n- Fundamentals: REST API design, Data Structures & Algorithms, Problem Solving`
    );
  };

  const loadSampleResumeText = () => {
    setResumeText(
      `Rahul Sharma - Computer Science & Engineering Graduate.\nEmail: rahul.demo@example.com | Phone: +1-555-019-2834\n\nOBJECTIVE\nMotivated B.Tech CSE student seeking a Full-Stack Software Engineering position.\n\nTECHNICAL SKILLS\n- Languages: Python, JavaScript, TypeScript, SQL, C++\n- Frameworks: React, Node.js, Express.js, FastAPI, Tailwind CSS\n- Databases: PostgreSQL, MongoDB, SQLite, Redis\n- DevOps & Cloud: Git, Docker, AWS (S3, EC2), Linux\n- Machine Learning & Fundamentals: scikit-learn, Pandas, NumPy, REST API, Object-Oriented Programming, Data Structures & Algorithms`
    );
  };

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    
    setSelectedFile(file);
    setUploading(true);
    setUploadStatus('Processing document & sanitizing PII...');
    setErrorMsg('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await api.uploadResume(formData);
      setUploadedResumeId(res.data.id);
      setUploadStatus(`File '${file.name}' uploaded successfully (${res.data.character_count} chars).`);
    } catch (err) {
      console.error("Upload error:", err);
      const detail = err.response?.data?.detail || "Document upload failed.";
      setErrorMsg(detail);
      setUploadStatus('');
    } finally {
      setUploading(false);
    }
  };

  const handleRunAnalysis = async () => {
    setErrorMsg('');
    if (!jobText || jobText.trim().length < 30) {
      setErrorMsg("Please enter a valid job description containing at least 30 characters.");
      return;
    }

    if (!uploadedResumeId && (!resumeText || resumeText.trim().length < 30)) {
      setErrorMsg("Please upload a resume file OR enter resume text.");
      return;
    }

    setAnalyzing(true);
    setAnalysisResult(null);

    const payload = {
      resume_id: uploadedResumeId || null,
      resume_text: uploadedResumeId ? null : resumeText,
      job_title: jobTitle,
      company_name: companyName,
      job_text: jobText
    };

    try {
      const res = await api.runAnalysis(payload);
      setAnalysisResult(res.data);
    } catch (err) {
      console.error("Analysis execution error:", err);
      const detail = err.response?.data?.detail || "Analysis failed to execute.";
      setErrorMsg(detail);
    } finally {
      setAnalyzing(false);
    }
  };

  const handleChecklistStatusUpdate = (itemId, newStatus) => {
    if (!analysisResult || !analysisResult.learning_checklist) return;
    const updated = analysisResult.learning_checklist.map((item) =>
      item.id === itemId ? { ...item, status: newStatus } : item
    );
    setAnalysisResult({ ...analysisResult, learning_checklist: updated });
  };

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-display font-bold text-white tracking-tight">
            Interactive NLP Resume & Job Analysis Engine
          </h1>
          <p className="text-sm text-slate-400">
            Compare candidate skills against target requirements using TF-IDF n-gram vectorization.
          </p>
        </div>
        <button
          onClick={() => {
            loadSampleJobText();
            loadSampleResumeText();
          }}
          className="self-start sm:self-auto inline-flex items-center space-x-2 text-xs font-medium text-teal-400 bg-teal-500/10 border border-teal-500/20 px-3 py-2 rounded-lg hover:bg-teal-500/20 transition-all cursor-pointer"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          <span>Load Sample Demo Data</span>
        </button>
      </div>

      {/* Error Alert */}
      {errorMsg && (
        <div className="bg-rose-500/10 border border-rose-500/30 rounded-xl p-4 flex items-start space-x-3 text-rose-300 text-sm">
          <AlertCircle className="w-5 h-5 text-rose-400 flex-shrink-0 mt-0.5" />
          <div>{errorMsg}</div>
        </div>
      )}

      {/* Input Dual Pane */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Resume Input Pane */}
        <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-display font-semibold text-white flex items-center gap-2">
              <FileText className="w-5 h-5 text-teal-400" /> Candidate Resume Input
            </h3>
            <span className="text-[11px] font-mono text-slate-400">PDF / DOCX / TXT</span>
          </div>

          {/* Upload Dropzone */}
          <div className="border-2 border-dashed border-slate-700/80 hover:border-teal-500/50 rounded-xl p-6 text-center space-y-3 bg-slate-900/40 transition-colors">
            <Upload className="w-8 h-8 text-teal-400 mx-auto" />
            <div className="space-y-1">
              <p className="text-sm font-medium text-slate-200">
                Upload Resume File (PDF, DOCX, TXT)
              </p>
              <p className="text-xs text-slate-400">Max size: 5MB &bull; Sensitive PII automatically masked</p>
            </div>
            <input
              type="file"
              accept=".pdf,.docx,.txt"
              onChange={handleFileUpload}
              className="hidden"
              id="resume-file-input"
            />
            <label
              htmlFor="resume-file-input"
              className="inline-block bg-slate-800 hover:bg-slate-700 text-teal-300 border border-teal-500/30 font-medium text-xs px-4 py-2 rounded-lg cursor-pointer transition-all"
            >
              {uploading ? 'Processing File...' : 'Choose Resume File'}
            </label>
            {uploadStatus && (
              <p className="text-xs text-emerald-400 font-mono mt-2">{uploadStatus}</p>
            )}
          </div>

          {/* Or Paste Raw Text */}
          <div className="space-y-2">
            <label className="text-xs text-slate-400 font-medium block">
              Or Edit / Paste Resume Text Content Directly:
            </label>
            <textarea
              rows={8}
              value={resumeText}
              onChange={(e) => {
                setResumeText(e.target.value);
                setUploadedResumeId(null);
              }}
              placeholder="Paste candidate resume text here..."
              className="w-full bg-slate-950/80 border border-slate-800 rounded-xl p-3 text-xs text-slate-200 focus:border-teal-500 focus:outline-none font-mono leading-relaxed resize-y"
            />
            <div className="flex justify-between text-[11px] text-slate-500">
              <span>Characters: {resumeText.length}</span>
              {uploadedResumeId && <span className="text-teal-400">Using Uploaded File</span>}
            </div>
          </div>
        </div>

        {/* Job Description Input Pane */}
        <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-display font-semibold text-white flex items-center gap-2">
              <Briefcase className="w-5 h-5 text-emerald-400" /> Target Job Description Input
            </h3>
            <span className="text-[11px] font-mono text-slate-400">Job Specs</span>
          </div>

          {/* Job Title & Company Fields */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="text-xs text-slate-400 font-medium mb-1 block flex items-center gap-1">
                <Briefcase className="w-3.5 h-3.5 text-teal-400" /> Job Title
              </label>
              <input
                type="text"
                value={jobTitle}
                onChange={(e) => setJobTitle(e.target.value)}
                placeholder="e.g. Full-Stack Software Engineer"
                className="w-full bg-slate-950/80 border border-slate-800 rounded-lg p-2.5 text-xs text-white focus:border-teal-500 focus:outline-none"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 font-medium mb-1 block flex items-center gap-1">
                <Building2 className="w-3.5 h-3.5 text-teal-400" /> Company Name (Optional)
              </label>
              <input
                type="text"
                value={companyName}
                onChange={(e) => setCompanyName(e.target.value)}
                placeholder="e.g. CloudScale Systems"
                className="w-full bg-slate-950/80 border border-slate-800 rounded-lg p-2.5 text-xs text-white focus:border-teal-500 focus:outline-none"
              />
            </div>
          </div>

          {/* Job Description Textarea */}
          <div className="space-y-2">
            <label className="text-xs text-slate-400 font-medium block">
              Job Description Specs & Skill Requirements:
            </label>
            <textarea
              rows={11}
              value={jobText}
              onChange={(e) => setJobText(e.target.value)}
              placeholder="Paste job description requirements..."
              className="w-full bg-slate-950/80 border border-slate-800 rounded-xl p-3 text-xs text-slate-200 focus:border-teal-500 focus:outline-none font-mono leading-relaxed resize-y"
            />
            <div className="flex justify-between text-[11px] text-slate-500">
              <span>Characters: {jobText.length}</span>
              <span>Minimum 30 required</span>
            </div>
          </div>
        </div>
      </div>

      {/* Analyze Trigger Button */}
      <div className="text-center pt-2">
        <button
          onClick={handleRunAnalysis}
          disabled={analyzing}
          className="inline-flex items-center space-x-3 bg-gradient-to-r from-teal-500 via-emerald-500 to-teal-600 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-bold text-base px-8 py-4 rounded-2xl shadow-xl shadow-teal-500/25 transition-all transform hover:-translate-y-0.5 cursor-pointer disabled:opacity-50"
        >
          {analyzing ? (
            <>
              <RefreshCw className="w-5 h-5 animate-spin" />
              <span>Running NLP Pipeline...</span>
            </>
          ) : (
            <>
              <FileSearch className="w-5 h-5" />
              <span>Execute Resume Analysis & Skill Matching</span>
            </>
          )}
        </button>
      </div>

      {/* Analysis Results Display */}
      {analysisResult && (
        <div className="space-y-8 animate-fadeIn pt-4">
          {/* Similarity Score Card */}
          <SimilarityGauge
            similarity={{
              percentage: analysisResult.similarity_percentage,
              similarity_score: analysisResult.similarity_score,
              level: analysisResult.similarity_level
            }}
            keywordBaseline={analysisResult.keyword_baseline_score}
          />

          {/* Skills Breakdown Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Matched Skills */}
            <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
              <div className="flex items-center justify-between pb-2 border-b border-slate-800">
                <h4 className="font-display font-semibold text-emerald-400 flex items-center gap-2">
                  <CheckCircle2 className="w-5 h-5" /> Matched Skills
                </h4>
                <span className="text-xs font-mono bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 px-2 py-0.5 rounded-full">
                  {analysisResult.matched_skills.length}
                </span>
              </div>
              <div className="flex flex-wrap gap-2 min-h-[100px] align-content-start">
                {analysisResult.matched_skills.length === 0 ? (
                  <p className="text-xs text-slate-500 italic">No matching skills identified.</p>
                ) : (
                  analysisResult.matched_skills.map((skill, i) => (
                    <SkillBadge key={i} skill={skill} type="matched" />
                  ))
                )}
              </div>
            </div>

            {/* Missing Skills */}
            <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
              <div className="flex items-center justify-between pb-2 border-b border-slate-800">
                <h4 className="font-display font-semibold text-amber-400 flex items-center gap-2">
                  <XCircle className="w-5 h-5" /> Missing Skill Gaps
                </h4>
                <span className="text-xs font-mono bg-amber-500/10 text-amber-300 border border-amber-500/20 px-2 py-0.5 rounded-full">
                  {analysisResult.missing_skills.length}
                </span>
              </div>
              <div className="flex flex-wrap gap-2 min-h-[100px] align-content-start">
                {analysisResult.missing_skills.length === 0 ? (
                  <p className="text-xs text-emerald-400 italic">Zero skill gaps found!</p>
                ) : (
                  analysisResult.missing_skills.map((skill, i) => (
                    <SkillBadge key={i} skill={skill} type="missing" />
                  ))
                )}
              </div>
            </div>

            {/* Resume Only Skills */}
            <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
              <div className="flex items-center justify-between pb-2 border-b border-slate-800">
                <h4 className="font-display font-semibold text-cyan-400 flex items-center gap-2">
                  <PlusCircle className="w-5 h-5" /> Additional Resume Skills
                </h4>
                <span className="text-xs font-mono bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 px-2 py-0.5 rounded-full">
                  {analysisResult.resume_only_skills.length}
                </span>
              </div>
              <div className="flex flex-wrap gap-2 min-h-[100px] align-content-start">
                {analysisResult.resume_only_skills.length === 0 ? (
                  <p className="text-xs text-slate-500 italic">No extra candidate skills listed.</p>
                ) : (
                  analysisResult.resume_only_skills.map((skill, i) => (
                    <SkillBadge key={i} skill={skill} type="resume_only" />
                  ))
                )}
              </div>
            </div>
          </div>

          {/* Learning Checklist Table */}
          <ChecklistTable
            items={analysisResult.learning_checklist}
            onStatusUpdate={handleChecklistStatusUpdate}
          />
        </div>
      )}
    </div>
  );
}
