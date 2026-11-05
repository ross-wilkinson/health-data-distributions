import React from 'react';
import { Database, ChevronRight, GraduationCap, AlertCircle, FileSpreadsheet } from 'lucide-react';
import type { MetricCatalogItem } from '../types/metric';

interface MetricCardProps {
  metric: MetricCatalogItem;
  onSelect: (id: string) => void;
}

export const MetricCard: React.FC<MetricCardProps> = ({ metric, onSelect }) => {
  const isAvailable = metric.status === 'available';

  return (
    <div
      onClick={() => isAvailable && onSelect(metric.id)}
      className={`group relative flex flex-col justify-between rounded-xl border bg-[var(--color-surface)] p-5 shadow-xs transition-all ${
        isAvailable
          ? 'cursor-pointer border-[var(--color-grid)] hover:border-[var(--color-series-1)] hover:shadow-md'
          : 'border-[var(--color-grid)]/60 opacity-80'
      }`}
    >
      <div>
        <div className="flex items-center justify-between gap-2">
          <span className="text-[11px] font-semibold uppercase tracking-wider text-[var(--color-ink-muted)]">
            {metric.category}
          </span>
          <span
            className={`inline-flex items-center rounded-full px-2 py-0.5 text-[11px] font-medium ${
              isAvailable
                ? 'bg-[var(--color-good)]/10 text-[var(--color-good)]'
                : 'bg-[var(--color-ink-muted)]/10 text-[var(--color-ink-muted)]'
            }`}
          >
            {isAvailable ? 'Available' : 'Planned'}
          </span>
        </div>

        <h3 className="mt-2 text-base font-bold text-[var(--color-ink)] group-hover:text-[var(--color-series-1)] transition-colors">
          {metric.name}
        </h3>

        <div className="mt-1 flex items-center gap-2">
          <span className="rounded-md bg-[var(--color-surface-subtle)] px-2 py-0.5 text-xs font-mono font-medium text-[var(--color-ink-secondary)]">
            {metric.units}
          </span>
          {metric.source_count > 0 && (
            <span className="flex items-center gap-1 text-xs text-[var(--color-ink-muted)]">
              <Database className="h-3 w-3" />
              <span>{metric.source_count} {metric.source_count === 1 ? 'source' : 'sources'}</span>
            </span>
          )}
        </div>

        <p className="mt-3 text-xs leading-relaxed text-[var(--color-ink-secondary)] line-clamp-2">
          {metric.definition}
        </p>

        {metric.academy_module && (
          <div className="mt-3 flex items-center gap-1.5 rounded-md bg-[var(--color-series-1)]/5 px-2 py-1 text-[11px] font-medium text-[var(--color-series-1)]">
            <GraduationCap className="h-3.5 w-3.5 shrink-0" />
            <span className="truncate">{metric.academy_module}</span>
          </div>
        )}

        {metric.methodological_warning && (
          <div className="mt-2 flex items-start gap-1.5 text-[11px] leading-tight text-[var(--color-warning)]">
            <AlertCircle className="h-3.5 w-3.5 shrink-0 mt-0.5" />
            <span className="line-clamp-2">{metric.methodological_warning}</span>
          </div>
        )}
      </div>

      <div className="mt-5 border-t border-[var(--color-grid)] pt-3 flex items-center justify-between text-xs">
        {isAvailable ? (
          <>
            <span className="inline-flex items-center gap-1 text-[var(--color-ink-muted)]">
              <FileSpreadsheet className="h-3.5 w-3.5" />
              <span>Tidy CSV &amp; JSON</span>
            </span>
            <span className="flex items-center gap-1 font-semibold text-[var(--color-series-1)] group-hover:translate-x-0.5 transition-transform">
              <span>Explore</span>
              <ChevronRight className="h-4 w-4" />
            </span>
          </>
        ) : (
          <span className="text-xs text-[var(--color-ink-muted)]">ETL pipeline scheduled</span>
        )}
      </div>
    </div>
  );
};
