import React, { useEffect, useState } from 'react';
import { 
  FileSearch, 
  History, 
  BookOpen, 
  BarChart3, 
  TrendingUp, 
  CheckCircle2, 
  AlertCircle, 
  ArrowRight,
  Cpu,
  Layers,
  Sparkles
} from 'lucide-react';
import { api } from '../services/api';

export default function Dashboard({ setActiveTab }) {
  const [analyses, setAnalyses] = useState([]);
  const [skillsCatalog, setSkillsCatalog] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboardData() {
      try {
        const [historyRes, skillsRes] = await Promise.all([
          api.getAnalyses(),
          api.getSkillsCatalog()
        ]);
        setAnalyses(historyRes.data || []);
        setSkillsCatalog(skillsRes.data || null);
      } catch (err) {
        console.error("Dashboard load error:", err);
      } finally {
        setLoading(false);
      }
    }
    loadDashboardData();
  }, []);

  const totalAnalyses = analyses.length;
  const avgScore = totalAnalyses > 0
    ? (analyses.reduce((acc, curr) => acc + curr.similarity_percentage, 0) / totalAnalyses).toFixed(1)
    : "0.0";

  const totalCatalogSkills = skillsCatalog
    ? Object.values(skillsCatalog.categories || {}).reduce((sum, list) => sum + list.length, 0)
    : 150;

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Top Banner */}
      <div className="relative overflow-hidden glass-panel rounded-3xl p-8 border border-slate-800 bg-gradient-to-r from-slate-900 via-slate-900/90 to-teal-950/40">
        <div className="relative z-10 max-w-3xl space-y-4">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-teal-500/10 border border-teal-500/20 text-teal-400 text-xs font-mono">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Academic BTech CSE Project NLP System</span>
          </div>
          <h1 className="text-3xl sm:text-4xl font-display font-extrabold text-white tracking-tight leading-tight">
            AI-Based Resume Screening & Job Matching System
          </h1>
          <p className="text-slate-300 text-sm sm:text-base leading-relaxed">
            Evaluate resume text similarity against job descriptions using reproducible TF-IDF vectorization, Cosine similarity, and phrase matching. Gain immediate insights into matched skills, identified gaps, and persistent learning roadmaps.
          </p>
          <div className="pt-2 flex flex-wrap gap-4">
            <button
              onClick={() => setActiveTab('analyze')}
              className="flex items-center space-x-2 bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-semibold px-6 py-3 rounded-xl transition-all shadow-lg shadow-teal-500/20 text-sm cursor-pointer"
            >
              <FileSearch className="w-4 h-4" />
              <span>Start Resume Matching</span>
              <ArrowRight className="w-4 h-4" />
            </button>
            <button
              onClick={() => setActiveTab('evaluation')}
              className="flex items-center space-x-2 bg-slate-800/80 hover:bg-slate-700/80 text-slate-200 border border-slate-700 font-medium px-5 py-3 rounded-xl transition-all text-sm cursor-pointer"
            >
              <BarChart3 className="w-4 h-4 text-teal-400" />
              <span>View Model Benchmarks</span>
            </button>
          </div>
        </div>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="glass-panel p-6 rounded-2xl border border-slate-800 flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-400">Total Analyses Executed</p>
            <h3 className="text-3xl font-display font-bold text-white mt-1">{totalAnalyses}</h3>
            <p className="text-[11px] text-teal-400 mt-1 flex items-center gap-1">
              <History className="w-3 h-3" /> Recorded in database
            </p>
          </div>
          <div className="p-3 rounded-xl bg-teal-500/10 text-teal-400 border border-teal-500/20">
            <Layers className="w-6 h-6" />
          </div>
        </div>

        <div className="glass-panel p-6 rounded-2xl border border-slate-800 flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-400">Avg Similarity Match</p>
            <h3 className="text-3xl font-display font-bold text-white mt-1">{avgScore}%</h3>
            <p className="text-[11px] text-emerald-400 mt-1 flex items-center gap-1">
              <TrendingUp className="w-3 h-3" /> TF-IDF Cosine Score
            </p>
          </div>
          <div className="p-3 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
            <BarChart3 className="w-6 h-6" />
          </div>
        </div>

        <div className="glass-panel p-6 rounded-2xl border border-slate-800 flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-400">Skill Catalog Dictionary</p>
            <h3 className="text-3xl font-display font-bold text-white mt-1">{totalCatalogSkills}+</h3>
            <p className="text-[11px] text-cyan-400 mt-1 flex items-center gap-1">
              <BookOpen className="w-3 h-3" /> Categorized technical terms
            </p>
          </div>
          <div className="p-3 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
            <BookOpen className="w-6 h-6" />
          </div>
        </div>

        <div className="glass-panel p-6 rounded-2xl border border-slate-800 flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-400">Privacy & PII Protection</p>
            <h3 className="text-xl font-display font-bold text-emerald-400 mt-1">100% Active</h3>
            <p className="text-[11px] text-slate-400 mt-1">Emails & numbers masked</p>
          </div>
          <div className="p-3 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/20">
            <Cpu className="w-6 h-6" />
          </div>
        </div>
      </div>

      {/* Quick Recent Activity Table */}
      <div className="glass-panel rounded-2xl border border-slate-800 p-6 space-y-4">
        <div className="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <h3 className="font-display font-semibold text-lg text-white">Recent Resume Analysis History</h3>
            <p className="text-xs text-slate-400">Latest NLP comparison runs stored in SQLite database.</p>
          </div>
          <button
            onClick={() => setActiveTab('history')}
            className="text-xs text-teal-400 hover:text-teal-300 font-medium flex items-center gap-1 cursor-pointer"
          >
            <span>View All ({totalAnalyses})</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        {loading ? (
          <div className="py-8 text-center text-slate-400 text-sm">Loading dashboard data...</div>
        ) : analyses.length === 0 ? (
          <div className="py-12 text-center space-y-3">
            <AlertCircle className="w-10 h-10 text-slate-600 mx-auto" />
            <p className="text-sm text-slate-400">No previous analyses found. Upload a resume to run your first evaluation.</p>
            <button
              onClick={() => setActiveTab('analyze')}
              className="inline-flex items-center space-x-2 bg-teal-500 hover:bg-teal-400 text-slate-950 font-semibold px-4 py-2 rounded-lg text-xs"
            >
              <span>Analyze Resume Now</span>
            </button>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm text-slate-300">
              <thead className="text-xs uppercase bg-slate-900/60 text-slate-400 border-b border-slate-800">
                <tr>
                  <th className="py-3 px-4 font-semibold">Job Title</th>
                  <th className="py-3 px-4 font-semibold">Company</th>
                  <th className="py-3 px-4 font-semibold">TF-IDF Similarity</th>
                  <th className="py-3 px-4 font-semibold">Matched Skills</th>
                  <th className="py-3 px-4 font-semibold">Missing Skills</th>
                  <th className="py-3 px-4 font-semibold">Date</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {analyses.slice(0, 5).map((row) => (
                  <tr key={row.id} className="hover:bg-slate-800/30 transition-colors">
                    <td className="py-3 px-4 font-medium text-white">{row.job_title}</td>
                    <td className="py-3 px-4 text-xs text-slate-400">{row.company_name || 'N/A'}</td>
                    <td className="py-3 px-4 font-mono font-semibold text-teal-400">
                      {row.similarity_percentage}%
                    </td>
                    <td className="py-3 px-4 text-xs text-emerald-400">
                      {row.skills_summary?.matched_count || row.matched_skills.length} skills
                    </td>
                    <td className="py-3 px-4 text-xs text-amber-400">
                      {row.skills_summary?.missing_count || row.missing_skills.length} skills
                    </td>
                    <td className="py-3 px-4 text-xs text-slate-500 font-mono">
                      {new Date(row.created_at).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
