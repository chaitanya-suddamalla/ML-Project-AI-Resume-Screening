import React, { useEffect, useState } from 'react';
import { 
  BarChart3, 
  Cpu, 
  Settings, 
  ShieldAlert, 
  CheckCircle2, 
  Layers, 
  HelpCircle,
  TrendingUp,
  FileCheck
} from 'lucide-react';
import { api } from '../services/api';

export default function ModelEvaluation() {
  const [evalData, setEvalData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadEvaluation() {
      try {
        const res = await api.getModelEvaluation();
        setEvalData(res.data || null);
      } catch (err) {
        console.error("Evaluation load error:", err);
      } finally {
        setLoading(false);
      }
    }
    loadEvaluation();
  }, []);

  if (loading) {
    return (
      <div className="glass-panel p-12 text-center text-slate-400 text-sm">
        Calculating model evaluation benchmarks...
      </div>
    );
  }

  const tfidf = evalData?.tfidf_configuration || {};
  const metrics = evalData?.overall_skill_extraction_metrics || {};
  const benchmarks = evalData?.benchmark_comparisons || [];
  const limitations = evalData?.model_limitations || [];

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div>
        <h1 className="text-2xl sm:text-3xl font-display font-bold text-white tracking-tight flex items-center gap-3">
          <BarChart3 className="w-7 h-7 text-teal-400" /> Model Evaluation & Benchmark Metrics
        </h1>
        <p className="text-sm text-slate-400">
          Transparent technical breakdown of TF-IDF hyperparameter settings, skill extraction metrics, baseline comparisons, and documented NLP limitations.
        </p>
      </div>

      {/* Metric Highlights */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <div className="glass-panel p-6 rounded-2xl border border-slate-800 text-center space-y-2">
          <span className="text-xs font-medium text-slate-400 uppercase tracking-wider">Average Skill Precision</span>
          <h3 className="text-3xl font-display font-extrabold text-emerald-400">{metrics.average_precision}</h3>
          <p className="text-[11px] text-slate-500">Exact phrase match reliability</p>
        </div>

        <div className="glass-panel p-6 rounded-2xl border border-slate-800 text-center space-y-2">
          <span className="text-xs font-medium text-slate-400 uppercase tracking-wider">Average Skill Recall</span>
          <h3 className="text-3xl font-display font-extrabold text-teal-400">{metrics.average_recall}</h3>
          <p className="text-[11px] text-slate-500">Coverage of requested requirements</p>
        </div>

        <div className="glass-panel p-6 rounded-2xl border border-slate-800 text-center space-y-2">
          <span className="text-xs font-medium text-slate-400 uppercase tracking-wider">Average F1-Score</span>
          <h3 className="text-3xl font-display font-extrabold text-cyan-400">{metrics.average_f1_score}</h3>
          <p className="text-[11px] text-slate-500">Harmonic mean on benchmark set</p>
        </div>
      </div>

      {/* TF-IDF Hyperparameter Configuration */}
      <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
        <div className="flex items-center space-x-2 pb-2 border-b border-slate-800">
          <Settings className="w-5 h-5 text-teal-400" />
          <h3 className="font-display font-semibold text-lg text-white">TF-IDF Vectorizer Hyperparameters</h3>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 space-y-1">
            <div className="flex justify-between items-center text-xs">
              <span className="font-semibold text-white">max_features</span>
              <span className="font-mono text-teal-400">{tfidf.max_features}</span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">{tfidf.max_features_explanation}</p>
          </div>

          <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 space-y-1">
            <div className="flex justify-between items-center text-xs">
              <span className="font-semibold text-white">ngram_range</span>
              <span className="font-mono text-teal-400">(1, 2) [Unigrams & Bigrams]</span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">{tfidf.ngram_range_explanation}</p>
          </div>

          <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 space-y-1">
            <div className="flex justify-between items-center text-xs">
              <span className="font-semibold text-white">stop_words</span>
              <span className="font-mono text-teal-400">english (Preserving tech tokens)</span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">{tfidf.stop_words_explanation}</p>
          </div>

          <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 space-y-1">
            <div className="flex justify-between items-center text-xs">
              <span className="font-semibold text-white">sublinear_tf</span>
              <span className="font-mono text-teal-400">True [1 + log(TF)]</span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">{tfidf.sublinear_tf_explanation}</p>
          </div>
        </div>
      </div>

      {/* Benchmark Comparisons Table */}
      <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
        <div className="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <h3 className="font-display font-semibold text-lg text-white flex items-center gap-2">
              <FileCheck className="w-5 h-5 text-emerald-400" /> Model Comparison Baseline Benchmark
            </h3>
            <p className="text-xs text-slate-400">
              Comparative analysis across Jaccard Keyword Overlap, TF-IDF Vector Cosine Similarity, and Sentence Transformers on labeled benchmark pairs.
            </p>
          </div>
          <span className="text-xs font-mono text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20">
            {benchmarks.length} Samples
          </span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm text-slate-300">
            <thead className="text-xs uppercase bg-slate-900/80 text-slate-400 border-b border-slate-800">
              <tr>
                <th className="py-3 px-4 font-semibold">Benchmark Sample</th>
                <th className="py-3 px-4 font-semibold">Job Title</th>
                <th className="py-3 px-4 font-semibold">Jaccard Keyword Baseline</th>
                <th className="py-3 px-4 font-semibold">TF-IDF Cosine Score</th>
                <th className="py-3 px-4 font-semibold">Semantic Embedding Score</th>
                <th className="py-3 px-4 font-semibold">Precision / Recall / F1</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {benchmarks.map((sample) => (
                <tr key={sample.id} className="hover:bg-slate-800/30 transition-colors">
                  <td className="py-4 px-4 font-semibold text-white">{sample.resume_title}</td>
                  <td className="py-4 px-4 text-xs text-slate-400">{sample.job_title}</td>
                  <td className="py-4 px-4 font-mono text-slate-400 text-xs">
                    {(sample.keyword_baseline_score * 100).toFixed(1)}%
                  </td>
                  <td className="py-4 px-4 font-mono font-bold text-teal-400">
                    {sample.tfidf_percentage}%
                  </td>
                  <td className="py-4 px-4 font-mono text-cyan-400 text-xs">
                    {sample.semantic_score ? `${(sample.semantic_score * 100).toFixed(1)}%` : 'Optional / Off'}
                  </td>
                  <td className="py-4 px-4 text-xs font-mono text-emerald-300">
                    P: {sample.skill_extraction_metrics.precision} | R: {sample.skill_extraction_metrics.recall} | F1: {sample.skill_extraction_metrics.f1_score}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Documented Limitations & Failure Cases */}
      <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
        <div className="flex items-center space-x-2 pb-2 border-b border-slate-800">
          <ShieldAlert className="w-5 h-5 text-amber-400" />
          <h3 className="font-display font-semibold text-lg text-white">Documented System Limitations & Known Failure Cases</h3>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {limitations.map((item, idx) => (
            <div key={idx} className="bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 space-y-2">
              <h4 className="font-semibold text-xs text-amber-300 flex items-center gap-1.5">
                <HelpCircle className="w-4 h-4 text-amber-400 flex-shrink-0" />
                {item.title}
              </h4>
              <p className="text-xs text-slate-400 leading-relaxed">{item.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
