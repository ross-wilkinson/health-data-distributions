import React, { useState } from 'react';
import {
  ArrowLeft,
  Download,
  Copy,
  Check,
  CheckCircle2,
  XCircle,
  FileText,
  ExternalLink,
} from 'lucide-react';
import type { MetricDetail, MetricSource } from '../types/metric';
import { MethodWarningBanner } from './MethodWarningBanner';
import { PercentileStrip } from './PercentileStrip';
import { MonkSwatchBar } from './MonkSwatchBar';

interface MetricDetailViewProps {
  metric: MetricDetail;
  onBack: () => void;
}

export const MetricDetailView: React.FC<MetricDetailViewProps> = ({ metric, onBack }) => {
  const [activeSourceId, setActiveSourceId] = useState<string>(metric.sources[0]?.id ?? '');
  const [selectedSubgroupIndex, setSelectedSubgroupIndex] = useState<number>(0);
  const [copiedType, setCopiedType] = useState<string | null>(null);

  const activeSource: MetricSource | undefined =
    metric.sources.find((s) => s.id === activeSourceId) ?? metric.sources[0];

  const handleCopy = (text: string, type: string) => {
    navigator.clipboard.writeText(text);
    setCopiedType(type);
    setTimeout(() => setCopiedType(null), 2000);
  };

  const handleCopyBibtex = async () => {
    if (!metric.bibtex_url) return;
    try {
      const res = await fetch(`.${metric.bibtex_url}`);
      const text = await res.text();
      handleCopy(text, 'bibtex');
    } catch {
      handleCopy(activeSource?.citation.text ?? '', 'citation');
    }
  };

  const isSkinTone = metric.id === 'skin_tone';

  return (
    <div className="space-y-8">
      {/* Top Navigation & Action Row */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <button
          type="button"
          onClick={onBack}
          className="inline-flex items-center gap-2 rounded-lg border border-[var(--color-grid)] bg-[var(--color-surface)] px-3 py-1.5 text-xs font-semibold text-[var(--color-ink)] hover:bg-[var(--color-surface-subtle)] transition-colors"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Back to Catalog</span>
        </button>

        <div className="flex flex-wrap items-center gap-2">
          {metric.tidy_csv_url && (
            <a
              href={`.${metric.tidy_csv_url}`}
              download
              className="inline-flex items-center gap-1.5 rounded-lg border border-[var(--color-grid)] bg-[var(--color-surface)] px-3 py-1.5 text-xs font-semibold text-[var(--color-ink)] hover:bg-[var(--color-surface-subtle)] transition-colors shadow-xs"
            >
              <Download className="h-3.5 w-3.5 text-[var(--color-series-1)]" />
              <span>Download Tidy CSV</span>
            </a>
          )}

          <button
            type="button"
            onClick={() => handleCopy(window.location.origin + `/data/metrics/${metric.id}.json`, 'api')}
            className="inline-flex items-center gap-1.5 rounded-lg border border-[var(--color-grid)] bg-[var(--color-surface)] px-3 py-1.5 text-xs font-semibold text-[var(--color-ink)] hover:bg-[var(--color-surface-subtle)] transition-colors shadow-xs"
          >
            {copiedType === 'api' ? <Check className="h-3.5 w-3.5 text-[var(--color-good)]" /> : <Copy className="h-3.5 w-3.5 text-[var(--color-series-2)]" />}
            <span>{copiedType === 'api' ? 'API URL Copied' : 'JSON API Endpoint'}</span>
          </button>

          <button
            type="button"
            onClick={handleCopyBibtex}
            className="inline-flex items-center gap-1.5 rounded-lg border border-[var(--color-grid)] bg-[var(--color-surface)] px-3 py-1.5 text-xs font-semibold text-[var(--color-ink)] hover:bg-[var(--color-surface-subtle)] transition-colors shadow-xs"
          >
            {copiedType === 'bibtex' ? <Check className="h-3.5 w-3.5 text-[var(--color-good)]" /> : <FileText className="h-3.5 w-3.5 text-[var(--color-series-3)]" />}
            <span>{copiedType === 'bibtex' ? 'BibTeX Copied!' : 'Copy BibTeX'}</span>
          </button>
        </div>
      </div>

      {/* Metric Header */}
      <div className="rounded-2xl border border-[var(--color-grid)] bg-[var(--color-surface)] p-6 sm:p-8 shadow-xs">
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded-md bg-[var(--color-series-1)]/10 px-2.5 py-1 text-xs font-bold uppercase tracking-wider text-[var(--color-series-1)]">
            {metric.category}
          </span>
          <span className="rounded-md bg-[var(--color-surface-subtle)] px-2.5 py-1 text-xs font-mono font-medium text-[var(--color-ink-secondary)]">
            {metric.units}
          </span>
          {metric.academy_module && (
            <span className="rounded-md bg-[var(--color-series-2)]/10 px-2.5 py-1 text-xs font-medium text-[var(--color-series-2)]">
              {metric.academy_module}
            </span>
          )}
        </div>

        <h1 className="mt-3 text-2xl font-black tracking-tight text-[var(--color-ink)] sm:text-3xl">
          {metric.name}
        </h1>

        <p className="mt-2 text-sm sm:text-base leading-relaxed text-[var(--color-ink-secondary)] max-w-4xl">
          {metric.definition}
        </p>

        {/* Epistemological Warning Banner */}
        {metric.methodological_warning && (
          <div className="mt-6">
            <MethodWarningBanner warning={metric.methodological_warning} />
          </div>
        )}
      </div>

      {/* Special Monk Swatch Palette for skin_tone */}
      {isSkinTone && (
        <div>
          <MonkSwatchBar />
        </div>
      )}

      {/* Sources Selection Tabs */}
      {metric.sources.length > 0 && (
        <div className="space-y-6">
          <div className="flex flex-col gap-2">
            <div className="text-xs font-bold uppercase tracking-wider text-[var(--color-ink-muted)]">
              Select Primary Source ({metric.sources.length} Available)
            </div>
            <div className="flex flex-wrap gap-2 border-b border-[var(--color-grid)] pb-3">
              {metric.sources.map((src) => {
                const isActive = src.id === activeSource?.id;
                return (
                  <button
                    key={src.id}
                    type="button"
                    onClick={() => {
                      setActiveSourceId(src.id);
                      setSelectedSubgroupIndex(0);
                    }}
                    className={`rounded-lg px-3 py-2 text-xs font-semibold transition-all ${
                      isActive
                        ? 'bg-[var(--color-ink)] text-[var(--color-surface)] shadow-xs'
                        : 'border border-[var(--color-grid)] bg-[var(--color-surface)] text-[var(--color-ink-secondary)] hover:bg-[var(--color-surface-subtle)]'
                    }`}
                  >
                    <span>{src.title}</span>
                    <span className="ml-1.5 text-[10px] opacity-75">
                      ({src.origin}{src.population.n ? `, n=${src.population.n.toLocaleString()}` : ''})
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Active Source Details */}
          {activeSource && (
            <div className="rounded-2xl border border-[var(--color-grid)] bg-[var(--color-surface)] p-6 shadow-xs space-y-6">
              <div className="flex flex-wrap items-center justify-between gap-3 border-b border-[var(--color-grid)] pb-4">
                <div>
                  <h3 className="text-lg font-bold text-[var(--color-ink)]">{activeSource.title}</h3>
                  <div className="text-xs text-[var(--color-ink-muted)]">
                    Origin: <span className="font-semibold text-[var(--color-ink)]">{activeSource.origin}</span> &bull;{' '}
                    Form: <span className="font-semibold text-[var(--color-ink)]">{activeSource.statistic_form}</span> &bull;{' '}
                    Sampling: <span className="font-semibold text-[var(--color-ink)]">{activeSource.population.sampling ?? 'N/A'}</span>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-xs text-[var(--color-ink-muted)]">Sample Size</div>
                  <div className="text-base font-mono font-bold text-[var(--color-ink)]">
                    {activeSource.population.n != null ? activeSource.population.n.toLocaleString() : 'N/A'}
                  </div>
                </div>
              </div>

              {/* Protocol & Population Breakdown */}
              <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 text-xs">
                <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-4">
                  <div className="font-bold text-[var(--color-ink)] mb-1">Measurement Protocol</div>
                  <div className="text-[var(--color-ink-secondary)] leading-relaxed">
                    {activeSource.measurement.method ?? 'Unspecified method'}
                  </div>
                  {activeSource.measurement.protocol && (
                    <div className="mt-2 text-[var(--color-ink-muted)]">
                      <strong>Procedure:</strong> {activeSource.measurement.protocol}
                    </div>
                  )}
                </div>

                <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-4">
                  <div className="font-bold text-[var(--color-ink)] mb-1">Target Population &amp; Exclusions</div>
                  <div className="text-[var(--color-ink-secondary)] leading-relaxed">
                    {activeSource.population.description ?? 'General cohort'}
                  </div>
                  {activeSource.population.exclusions && (
                    <div className="mt-2 text-[var(--color-ink-muted)]">
                      <strong>Exclusions:</strong> {activeSource.population.exclusions}
                    </div>
                  )}
                </div>
              </div>

              {/* Interactive Percentile Visualizer Strip */}
              {activeSource.subgroups[selectedSubgroupIndex] && (
                <div className="space-y-3">
                  <PercentileStrip
                    summary={activeSource.subgroups[selectedSubgroupIndex].summary}
                    units={metric.units}
                    subgroupLabel={Object.values(activeSource.subgroups[selectedSubgroupIndex].subgroup).join(' / ') || 'Overall'}
                  />
                </div>
              )}

              {/* Subgroup Distribution Table */}
              {activeSource.subgroups.length > 0 ? (
                <div>
                  <div className="mb-2 flex items-center justify-between">
                    <div className="text-xs font-bold uppercase tracking-wider text-[var(--color-ink-muted)]">
                      Empirical Subgroup Breakdown (Click row to inspect spread)
                    </div>
                    <div className="text-xs text-[var(--color-ink-muted)]">
                      {activeSource.subgroups.length} subgroups
                    </div>
                  </div>

                  <div className="overflow-x-auto rounded-xl border border-[var(--color-grid)]">
                    <table className="w-full text-left text-xs border-collapse">
                      <thead>
                        <tr className="border-b border-[var(--color-grid)] bg-[var(--color-surface-subtle)] text-[var(--color-ink-muted)]">
                          {activeSource.subgroup_columns.map((col) => (
                            <th key={col} className="p-3 font-semibold uppercase tracking-wider">
                              {col.replace('_', ' ')}
                            </th>
                          ))}
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">n</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">Mean (95% CI)</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">&sigma;<sub>b</sub> (SD)</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">P5</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">P25</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider font-bold text-[var(--color-series-1)]">Median</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">P75</th>
                          <th className="p-3 text-right font-semibold uppercase tracking-wider">P95</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-[var(--color-grid)]">
                        {activeSource.subgroups.map((sg, idx) => {
                          const isSelected = idx === selectedSubgroupIndex;
                          const meanVal = sg.statistics['mean']?.estimate;
                          const meanCi = sg.summary.ci_mean;
                          const sdVal = sg.statistics['sd']?.estimate;

                          return (
                            <tr
                              key={idx}
                              onClick={() => setSelectedSubgroupIndex(idx)}
                              className={`cursor-pointer transition-colors ${
                                isSelected
                                  ? 'bg-[var(--color-series-1)]/10 font-medium'
                                  : 'hover:bg-[var(--color-surface-subtle)]'
                              }`}
                            >
                              {activeSource.subgroup_columns.map((col) => (
                                <td key={col} className="p-3 font-medium text-[var(--color-ink)]">
                                  {sg.subgroup[col] ?? 'All'}
                                </td>
                              ))}
                              <td className="p-3 text-right font-mono text-[var(--color-ink-secondary)]">
                                {sg.n?.toLocaleString() ?? '-'}
                              </td>
                              <td className="p-3 text-right font-mono text-[var(--color-ink)]">
                                {meanVal != null
                                  ? `${meanVal}${meanCi ? ` (${meanCi[0]}–${meanCi[1]})` : ''}`
                                  : '-'}
                              </td>
                              <td className="p-3 text-right font-mono text-[var(--color-ink)]">
                                {sdVal != null ? sdVal : '-'}
                              </td>
                              <td className="p-3 text-right font-mono text-[var(--color-ink-muted)]">
                                {sg.statistics['p5']?.estimate ?? '-'}
                              </td>
                              <td className="p-3 text-right font-mono text-[var(--color-ink-muted)]">
                                {sg.statistics['p25']?.estimate ?? '-'}
                              </td>
                              <td className="p-3 text-right font-mono font-bold text-[var(--color-series-1)]">
                                {sg.statistics['p50']?.estimate ?? '-'}
                              </td>
                              <td className="p-3 text-right font-mono text-[var(--color-ink-muted)]">
                                {sg.statistics['p75']?.estimate ?? '-'}
                              </td>
                              <td className="p-3 text-right font-mono text-[var(--color-ink-muted)]">
                                {sg.statistics['p95']?.estimate ?? '-'}
                              </td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                </div>
              ) : (
                <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-6 text-center text-xs text-[var(--color-ink-muted)]">
                  This source records documented literature moments or gap findings. Full individual subgroups were not tabulated.
                </div>
              )}

              {/* Fit-for-Purpose Decision Guidance */}
              <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 pt-2">
                <div className="rounded-xl border border-[var(--color-good)]/30 bg-[var(--color-good)]/5 p-4 text-xs">
                  <div className="flex items-center gap-1.5 font-bold text-[var(--color-good)] mb-2">
                    <CheckCircle2 className="h-4 w-4" />
                    <span>Legitimate Use Cases (Use For)</span>
                  </div>
                  <ul className="space-y-1 text-[var(--color-ink-secondary)] leading-relaxed list-disc list-inside">
                    {activeSource.use_for.map((u, i) => (
                      <li key={i}>{u}</li>
                    ))}
                  </ul>
                </div>

                <div className="rounded-xl border border-[var(--color-critical)]/30 bg-[var(--color-critical)]/5 p-4 text-xs">
                  <div className="flex items-center gap-1.5 font-bold text-[var(--color-critical)] mb-2">
                    <XCircle className="h-4 w-4" />
                    <span>Strict Epistemological Boundaries (Do NOT Use For)</span>
                  </div>
                  <ul className="space-y-1 text-[var(--color-ink-secondary)] leading-relaxed list-disc list-inside">
                    {activeSource.do_not_use_for.map((d, i) => (
                      <li key={i}>{d}</li>
                    ))}
                  </ul>
                </div>
              </div>

              {/* Caveats */}
              {activeSource.caveats.length > 0 && (
                <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-4 text-xs space-y-2">
                  <div className="font-bold text-[var(--color-ink)]">Methodological Caveats</div>
                  <ul className="space-y-1.5 text-[var(--color-ink-secondary)] leading-relaxed list-disc list-inside">
                    {activeSource.caveats.map((c, i) => (
                      <li key={i} dangerouslySetInnerHTML={{ __html: c.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') }} />
                    ))}
                  </ul>
                </div>
              )}

              {/* Primary Literature Citation */}
              <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-4 text-xs space-y-2">
                <div className="flex items-center justify-between">
                  <div className="font-bold text-[var(--color-ink)]">Primary Citation &amp; License</div>
                  {activeSource.citation.url && (
                    <a
                      href={activeSource.citation.url}
                      target="_blank"
                      rel="noreferrer"
                      className="inline-flex items-center gap-1 text-[var(--color-series-1)] hover:underline"
                    >
                      <span>Primary Source</span>
                      <ExternalLink className="h-3 w-3" />
                    </a>
                  )}
                </div>
                <blockquote className="border-l-2 border-[var(--color-series-1)] pl-3 italic text-[var(--color-ink)]">
                  {activeSource.citation.text}
                </blockquote>
                <div className="text-[11px] text-[var(--color-ink-muted)]">
                  <strong>Terms / License:</strong> {activeSource.citation.license ?? 'Public use data file'}
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
