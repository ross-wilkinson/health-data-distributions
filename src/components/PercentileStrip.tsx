import React from 'react';
import type { SubgroupSummary } from '../types/metric';

interface PercentileStripProps {
  summary: SubgroupSummary;
  units: string;
  subgroupLabel: string;
}

export const PercentileStrip: React.FC<PercentileStripProps> = ({
  summary,
  units,
  subgroupLabel,
}) => {
  const p5 = summary.p5;
  const p25 = summary.p25;
  const p50 = summary.median;
  const p75 = summary.p75;
  const p95 = summary.p95;

  if (p5 == null || p25 == null || p50 == null || p75 == null || p95 == null) {
    if (summary.mean != null && summary.sd != null) {
      return (
        <div className="rounded-lg border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-4 text-center text-xs text-[var(--color-ink-muted)]">
          <span className="font-semibold text-[var(--color-ink)]">{subgroupLabel}</span>: Reported as Moments only &bull; Mean:{' '}
          <span className="font-mono font-bold text-[var(--color-ink)]">{summary.mean}</span> {units} &plusmn;{' '}
          <span className="font-mono font-bold text-[var(--color-ink)]">{summary.sd}</span> {units} (No empirical percentiles reported).
        </div>
      );
    }
    return null;
  }

  // Dynamic range with padding
  const spanMin = Math.floor(p5 - (p95 - p5) * 0.15);
  const spanMax = Math.ceil(p95 + (p95 - p5) * 0.15);
  const range = spanMax - spanMin || 1;

  const toPct = (val: number) => Math.max(0, Math.min(100, ((val - spanMin) / range) * 100));

  const leftIQR = toPct(p25);
  const widthIQR = Math.max(2, toPct(p75) - leftIQR);
  const leftMedian = toPct(p50);
  const leftP5 = toPct(p5);
  const leftP95 = toPct(p95);

  return (
    <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-4 transition-colors">
      <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
        <span className="font-semibold text-[var(--color-ink)]">
          Percentile Spread: <span className="text-[var(--color-series-1)]">{subgroupLabel}</span>
        </span>
        <span className="font-mono font-medium text-[var(--color-ink-secondary)]">
          IQR [{p25} – {p75}] {units} &bull; Median: {p50} {units}
        </span>
      </div>

      <div className="relative my-6 h-8 w-full rounded-md bg-[var(--color-grid)]">
        {/* Whiskers (P5 to P95) */}
        <div
          className="absolute top-1/2 h-0.5 -translate-y-1/2 bg-[var(--color-ink-muted)]"
          style={{ left: `${leftP5}%`, width: `${leftP95 - leftP5}%` }}
        />

        {/* P5 cap */}
        <div
          className="absolute top-1.5 h-5 w-0.5 -translate-x-1/2 bg-[var(--color-ink-muted)]"
          style={{ left: `${leftP5}%` }}
          title={`P5: ${p5} ${units}`}
        />

        {/* P95 cap */}
        <div
          className="absolute top-1.5 h-5 w-0.5 -translate-x-1/2 bg-[var(--color-ink-muted)]"
          style={{ left: `${leftP95}%` }}
          title={`P95: ${p95} ${units}`}
        />

        {/* IQR Box (P25 to P75) */}
        <div
          className="absolute top-1 bottom-1 rounded-sm bg-[var(--color-series-1)]/30 border border-[var(--color-series-1)]"
          style={{ left: `${leftIQR}%`, width: `${widthIQR}%` }}
          title={`IQR: [${p25} – ${p75}]`}
        />

        {/* Median bar */}
        <div
          className="absolute top-0 bottom-0 w-1 -translate-x-1/2 bg-[var(--color-series-1)] rounded-full shadow-xs"
          style={{ left: `${leftMedian}%` }}
          title={`Median (P50): ${p50} ${units}`}
        />

        {/* Labels below */}
        <div
          className="absolute -bottom-5 text-[10px] font-mono text-[var(--color-ink-muted)] -translate-x-1/2"
          style={{ left: `${leftP5}%` }}
        >
          {p5}
        </div>
        <div
          className="absolute -bottom-5 text-[10px] font-mono font-semibold text-[var(--color-series-1)] -translate-x-1/2"
          style={{ left: `${leftMedian}%` }}
        >
          {p50}
        </div>
        <div
          className="absolute -bottom-5 text-[10px] font-mono text-[var(--color-ink-muted)] -translate-x-1/2"
          style={{ left: `${leftP95}%` }}
        >
          {p95}
        </div>
      </div>
    </div>
  );
};
