export interface SourceSummary {
  id: string;
  title: string;
  origin: 'recomputed' | 'transcribed' | 'digitised' | 'gap';
  statistic_form: 'percentiles' | 'moments' | 'proportions' | 'none';
  group?: string | null;
  n?: number | null;
}

export interface MetricCatalogItem {
  id: string;
  name: string;
  category: string;
  units: string;
  priority: number;
  status: 'available' | 'planned';
  definition: string;
  source_count: number;
  sources: SourceSummary[];
  academy_module?: string;
  methodological_warning?: string;
}

export interface CatalogPayload {
  version: string;
  generated_at: string;
  total_metrics: number;
  available_metrics: number;
  planned_metrics: number;
  metrics: MetricCatalogItem[];
}

export interface StatItem {
  estimate: number | null;
  ci_low?: number | null;
  ci_high?: number | null;
}

export interface SubgroupSummary {
  mean?: number | null;
  ci_mean?: [number, number] | null;
  sd?: number | null;
  median?: number | null;
  iqr?: number | null;
  p25?: number | null;
  p75?: number | null;
  p5?: number | null;
  p95?: number | null;
  proportion?: number | null;
  ci_proportion?: [number, number] | null;
}

export interface SubgroupItem {
  subgroup: Record<string, string>;
  n: number | null;
  statistics: Record<string, StatItem>;
  summary: SubgroupSummary;
}

export interface MetricSource {
  id: string;
  title: string;
  origin: 'recomputed' | 'transcribed' | 'digitised' | 'gap';
  statistic_form: 'percentiles' | 'moments' | 'proportions' | 'none';
  group?: string | null;
  population: {
    description?: string;
    country?: string;
    years?: string;
    age_range?: string;
    n?: number | null;
    n_eligible?: number | null;
    sampling?: string;
    exclusions?: string;
  };
  measurement: {
    method?: string;
    device?: string;
    protocol?: string;
  };
  analysis: string[];
  use_for: string[];
  do_not_use_for: string[];
  caveats: string[];
  review_status: 'draft' | 'reviewed';
  citation: {
    text: string;
    url?: string;
    doi?: string;
    license?: string;
  };
  provenance: Record<string, unknown>;
  verification?: string;
  subgroup_columns: string[];
  subgroups: SubgroupItem[];
}

export interface MetricDetail {
  id: string;
  name: string;
  category: string;
  units: string;
  priority: number;
  status: 'available' | 'planned';
  definition: string;
  comparison_note?: string;
  methodological_warning?: string;
  academy_module?: string;
  candidate_sources?: string[];
  sources: MetricSource[];
  tidy_csv_url?: string | null;
  bibtex_url?: string | null;
}
