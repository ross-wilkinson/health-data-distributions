import React from 'react';
import { AlertTriangle, AlertCircle } from 'lucide-react';

interface MethodWarningBannerProps {
  warning: string;
  title?: string;
  compact?: boolean;
}

export const MethodWarningBanner: React.FC<MethodWarningBannerProps> = ({
  warning,
  title = 'When NOT to Pool: Measurement Method is Part of the Data',
  compact = false,
}) => {
  return (
    <div
      className={`rounded-xl border border-[var(--color-warning)]/30 bg-[var(--color-warning)]/10 text-[var(--color-ink)] transition-colors ${
        compact ? 'p-3' : 'p-4 sm:p-5'
      }`}
    >
      <div className="flex items-start gap-3">
        <div className="flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-[var(--color-warning)]/20 text-[var(--color-warning)]">
          {compact ? <AlertCircle className="h-4 w-4" /> : <AlertTriangle className="h-4 w-4" />}
        </div>
        <div>
          <div className="text-sm font-bold tracking-tight text-[var(--color-ink)]">{title}</div>
          <div className="mt-1 text-xs sm:text-sm leading-relaxed text-[var(--color-ink-secondary)]">
            {warning}
          </div>
        </div>
      </div>
    </div>
  );
};
