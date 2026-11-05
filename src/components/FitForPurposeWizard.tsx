import React, { useState } from 'react';
import { HelpCircle, CheckCircle, XCircle, Sparkles, ExternalLink } from 'lucide-react';

interface WizardState {
  deviceType: 'wearable_wrist' | 'clinic_spot' | 'patch_ecg';
  goal: 'pivotal_sizing' | 'firmware_parity' | 'demographic_quota' | 'longitudinal_baseline';
  demographic: 'general_adult' | 'dark_skin' | 'elderly';
}

export const FitForPurposeWizard: React.FC = () => {
  const [deviceType, setDeviceType] = useState<WizardState['deviceType']>('wearable_wrist');
  const [goal, setGoal] = useState<WizardState['goal']>('pivotal_sizing');
  const [demographic, setDemographic] = useState<WizardState['demographic']>('general_adult');

  const getRecommendation = () => {
    if (goal === 'demographic_quota' || demographic === 'dark_skin') {
      return {
        verdict: 'Use Google SCIN & NHANES 2003–2004 Dermatology Photographic Exams',
        recommendedSigma: 'N/A (Proportions scale)',
        metricId: 'skin_tone',
        useSource: 'Google SCIN multi-annotator Monk scores & NHANES reader-assigned Fitzpatrick',
        avoidSource: 'Pichon 2010 self-reported burning/tanning questions (59% non-response among Black adults)',
        academyModule: 'Module 4: Demographic Equity & The Regulatory Quota Trap (ISO 80601-2-61)',
        rationale:
          'Self-reported sun-burning questionnaires systematically break down in darker skin tones. Optical melanin attenuation is physical photon absorption (530 nm green PPG), requiring standalone empirical bounds without Bayesian hierarchical shrinkage (ADR-006).',
      };
    }

    if (deviceType === 'wearable_wrist' && goal === 'pivotal_sizing') {
      return {
        verdict: 'Use Quer et al. 2020 Fitbit Cohort (Longitudinal Wearable)',
        recommendedSigma: '7.7 bpm (Between-subject)',
        metricId: 'resting_heart_rate',
        useSource: 'Quer et al. 2020 (n = 92,457 device owners)',
        avoidSource: 'NHANES Seated Clinic Pulse (11.7 bpm)',
        academyModule: 'Module 3: Clustered Repeated Measures & Variance Decomposition',
        rationale:
          'Do NOT use clinic pulse to size a continuous wearable trial. The 11.7 bpm clinic variance includes acute white-coat anxiety and discrete 30s counting noise. Using clinic variance will inflate required study sample size by over 75%.',
      };
    }

    if (deviceType === 'wearable_wrist' && goal === 'firmware_parity') {
      return {
        verdict: 'Exploit Paired Correlation Dividend on Historical Optical Recordings',
        recommendedSigma: 'sigma_pair = sqrt(2 * sigma^2 * (1 - rho))',
        metricId: 'resting_heart_rate',
        useSource: 'Historical paired optical streams (rho >= 0.95)',
        avoidSource: 'Unpaired population reference tables',
        academyModule: 'Module 2: The Paired Correlation Dividend (Firmware Updates)',
        rationale:
          'Because both algorithms evaluate identical optical sensor streams, correlation is extreme. Sizing as independent groups requires N=190; sizing with paired variance reduces enrollment to N=10–12.',
      };
    }

    if (deviceType === 'clinic_spot') {
      return {
        verdict: 'Use NHANES 2015–2018 Seated Clinic Pulse (Survey Weighted)',
        recommendedSigma: '11.69 bpm (General adult population)',
        metricId: 'resting_heart_rate',
        useSource: 'NHANES 2015–2018 (n = 10,848, probability sample)',
        avoidSource: 'Fitbit or Apple Watch continuous waking cohorts',
        academyModule: 'Module 7: Two-Gate 4-Quadrant Clinical Verification',
        rationale:
          'NHANES probability sample accurately captures clinic triage examination conditions without exclusions for cardiovascular medications, arrhythmias, or BMI extremes.',
      };
    }

    return {
      verdict: 'Use NHANES Probability Sample with Stratified Subgroup Disclosures',
      recommendedSigma: '11.4 – 12.0 bpm',
      metricId: 'resting_heart_rate',
      useSource: 'NHANES 2015–2018 Probability Survey',
      avoidSource: 'Convenience cohorts with self-selection bias',
      academyModule: 'Module 3: HIIT Repeated Measures & Variance Decomposition',
      rationale:
        'General clinical protocol sizing requires representative probability sampling to ensure generalizability across age brackets and health comorbidities.',
    };
  };

  const rec = getRecommendation();

  return (
    <div className="rounded-2xl border border-[var(--color-grid)] bg-[var(--color-surface)] p-6 sm:p-8 shadow-xs space-y-6">
      <div className="border-b border-[var(--color-grid)] pb-5">
        <div className="inline-flex items-center gap-1.5 rounded-md bg-[var(--color-series-1)]/10 px-2 py-0.5 text-xs font-bold text-[var(--color-series-1)]">
          <HelpCircle className="h-3.5 w-3.5" />
          <span>Protocol Suitability Engine</span>
        </div>
        <h2 className="mt-2 text-xl font-black tracking-tight text-[var(--color-ink)]">
          Can I Use This Data for My Research?
        </h2>
        <p className="mt-1 text-xs text-[var(--color-ink-secondary)]">
          Answer 3 protocol questions to determine which empirical distribution fits your study and when pooling is prohibited.
        </p>
      </div>

      {/* Selectors */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
        <div>
          <label className="block text-xs font-bold text-[var(--color-ink)] mb-1.5">
            1. Target Device Form Factor
          </label>
          <select
            value={deviceType}
            onChange={(e) => setDeviceType(e.target.value as WizardState['deviceType'])}
            className="w-full rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] px-3 py-2 text-xs font-medium text-[var(--color-ink)] focus:border-[var(--color-series-1)]"
          >
            <option value="wearable_wrist">Wrist Wearable (Continuous Optical PPG)</option>
            <option value="clinic_spot">Spot-Check Clinic Monitor (Cuff / SpO2 clip)</option>
            <option value="patch_ecg">Chest Patch / Ambulatory Holter ECG</option>
          </select>
        </div>

        <div>
          <label className="block text-xs font-bold text-[var(--color-ink)] mb-1.5">
            2. Validation Objective
          </label>
          <select
            value={goal}
            onChange={(e) => setGoal(e.target.value as WizardState['goal'])}
            className="w-full rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] px-3 py-2 text-xs font-medium text-[var(--color-ink)] focus:border-[var(--color-series-1)]"
          >
            <option value="pivotal_sizing">Pivotal Trial Sample Sizing (FDA 510(k))</option>
            <option value="firmware_parity">Paired Algorithm Update (Firmware V2 vs V1)</option>
            <option value="demographic_quota">Demographic Inclusivity Quotas (ISO 80601)</option>
            <option value="longitudinal_baseline">Longitudinal Baselines &amp; Drift Canary</option>
          </select>
        </div>

        <div>
          <label className="block text-xs font-bold text-[var(--color-ink)] mb-1.5">
            3. Target Cohort
          </label>
          <select
            value={demographic}
            onChange={(e) => setDemographic(e.target.value as WizardState['demographic'])}
            className="w-full rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] px-3 py-2 text-xs font-medium text-[var(--color-ink)] focus:border-[var(--color-series-1)]"
          >
            <option value="general_adult">General US Adult Population (18+)</option>
            <option value="dark_skin">High-Melanin / Dark Skin Tones (MST 7–10)</option>
            <option value="elderly">Elderly &amp; Comorbid Cohort (65+)</option>
          </select>
        </div>
      </div>

      {/* Decision Output Card */}
      <div className="rounded-xl border border-[var(--color-series-1)]/30 bg-[var(--color-series-1)]/5 p-5 space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[var(--color-series-1)]/20 pb-3">
          <div className="flex items-center gap-2">
            <Sparkles className="h-4 w-4 text-[var(--color-series-1)]" />
            <span className="text-xs font-bold uppercase tracking-wider text-[var(--color-series-1)]">
              Epistemological Verdict
            </span>
          </div>
          <a
            href="https://ross-wilkinson.github.io/validation-study-designer/#/curriculum"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-1 text-[11px] font-semibold text-[var(--color-series-1)] hover:underline"
          >
            <span>{rec.academyModule}</span>
            <ExternalLink className="h-3 w-3" />
          </a>
        </div>

        <div className="text-base font-bold text-[var(--color-ink)]">
          {rec.verdict}
        </div>

        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 text-xs">
          <div className="rounded-lg bg-[var(--color-surface)] p-3 border border-[var(--color-grid)] space-y-1">
            <div className="flex items-center gap-1.5 font-bold text-[var(--color-good)]">
              <CheckCircle className="h-3.5 w-3.5" />
              <span>Recommended Source to Pull</span>
            </div>
            <div className="text-[var(--color-ink)] font-medium">{rec.useSource}</div>
            <div className="text-[11px] text-[var(--color-ink-muted)]">
              Sizing parameter: <strong>&sigma;<sub>b</sub> = {rec.recommendedSigma}</strong>
            </div>
          </div>

          <div className="rounded-lg bg-[var(--color-surface)] p-3 border border-[var(--color-grid)] space-y-1">
            <div className="flex items-center gap-1.5 font-bold text-[var(--color-critical)]">
              <XCircle className="h-3.5 w-3.5" />
              <span>Strict Disallowance (Do NOT Pool)</span>
            </div>
            <div className="text-[var(--color-ink)] font-medium">{rec.avoidSource}</div>
            <div className="text-[11px] text-[var(--color-critical)] font-medium">
              Pooling will invalidate protocol sample sizing.
            </div>
          </div>
        </div>

        <div className="rounded-lg bg-[var(--color-surface)]/80 p-3 text-xs leading-relaxed text-[var(--color-ink-secondary)] border border-[var(--color-grid)]">
          <strong>Scientific Rationale:</strong> {rec.rationale}
        </div>
      </div>
    </div>
  );
};
