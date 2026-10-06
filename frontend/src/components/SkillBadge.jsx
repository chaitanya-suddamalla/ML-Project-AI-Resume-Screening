import React from 'react';
import { CheckCircle2, XCircle, PlusCircle, Sparkles } from 'lucide-react';

export default function SkillBadge({ skill, type = 'matched' }) {
  const name = skill.name || skill;
  const category = skill.category || 'General';
  const matchType = skill.match_type || 'exact';

  if (type === 'matched') {
    return (
      <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/25 text-emerald-300 text-xs font-medium group transition-all hover:bg-emerald-500/15">
        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 flex-shrink-0" />
        <span>{name}</span>
        <span className="text-[10px] text-emerald-400/70 font-mono bg-emerald-950/60 px-1.5 py-0.5 rounded border border-emerald-800/40">
          {category}
        </span>
        {matchType === 'synonym/inferred' && (
          <span className="text-[9px] text-teal-300 bg-teal-900/60 px-1 rounded flex items-center gap-0.5" title="Inferred from synonym mapping">
            <Sparkles className="w-2.5 h-2.5" /> Synonym
          </span>
        )}
      </div>
    );
  }

  if (type === 'missing') {
    return (
      <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/25 text-amber-300 text-xs font-medium transition-all hover:bg-amber-500/15">
        <XCircle className="w-3.5 h-3.5 text-amber-400 flex-shrink-0" />
        <span>{name}</span>
        <span className="text-[10px] text-amber-400/70 font-mono bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-800/40">
          {category}
        </span>
      </div>
    );
  }

  return (
    <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-cyan-500/10 border border-cyan-500/25 text-cyan-300 text-xs font-medium transition-all hover:bg-cyan-500/15">
      <PlusCircle className="w-3.5 h-3.5 text-cyan-400 flex-shrink-0" />
      <span>{name}</span>
      <span className="text-[10px] text-cyan-400/70 font-mono bg-cyan-950/60 px-1.5 py-0.5 rounded border border-cyan-800/40">
        {category}
      </span>
    </div>
  );
}
