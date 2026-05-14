import json
import math
import os
from collections import defaultdict
from typing import Dict, List


# ==============================
# Metric Functions
# ==============================

def precision_at_k(ranked_list: List[int], qrels: Dict[str, int], k: int) -> float:
    ranked_list = ranked_list[:k]
    if not ranked_list:
        return 0.0

    relevant = sum(1 for doc_id in ranked_list if qrels.get(str(doc_id), 0) > 0)
    return relevant / k


def recall_at_k(ranked_list: List[int], qrels: Dict[str, int], k: int) -> float:
    ranked_list = ranked_list[:k]
    total_relevant = sum(1 for rel in qrels.values() if rel > 0)

    if total_relevant == 0:
        return 0.0

    retrieved_relevant = sum(1 for doc_id in ranked_list if qrels.get(str(doc_id), 0) > 0)
    return retrieved_relevant / total_relevant


def reciprocal_rank(ranked_list: List[int], qrels: Dict[str, int]) -> float:
    for rank, doc_id in enumerate(ranked_list, start=1):
        if qrels.get(str(doc_id), 0) > 0:
            return 1.0 / rank
    return 0.0


def dcg_at_k(ranked_list: List[int], qrels: Dict[str, int], k: int) -> float:
    dcg = 0.0
    for i, doc_id in enumerate(ranked_list[:k]):
        rel = qrels.get(str(doc_id), 0)
        dcg += (2**rel - 1) / math.log2(i + 2)
    return dcg


def ndcg_at_k(ranked_list: List[int], qrels: Dict[str, int], k: int) -> float:
    dcg = dcg_at_k(ranked_list, qrels, k)

    # Ideal DCG
    ideal_rels = sorted(qrels.values(), reverse=True)
    ideal_dcg = 0.0
    for i, rel in enumerate(ideal_rels[:k]):
        ideal_dcg += (2**rel - 1) / math.log2(i + 2)

    if ideal_dcg == 0:
        return 0.0

    return dcg / ideal_dcg


# ==============================
# Evaluation Function
# ==============================

def evaluate_system(run: Dict[str, List[int]],
                    qrels: Dict[str, Dict[str, int]],
                    k_values: List[int]) -> Dict[str, float]:

    results = defaultdict(list)

    for query_id, ranked_list in run.items():
        if query_id not in qrels:
            continue

        query_qrels = qrels[query_id]

        for k in k_values:
            results[f"P@{k}"].append(
                precision_at_k(ranked_list, query_qrels, k)
            )
            results[f"R@{k}"].append(
                recall_at_k(ranked_list, query_qrels, k)
            )
            results[f"nDCG@{k}"].append(
                ndcg_at_k(ranked_list, query_qrels, k)
            )

        results["MRR"].append(
            reciprocal_rank(ranked_list, query_qrels)
        )

    # Average over queries
    final_scores = {}
    for metric, values in results.items():
        final_scores[metric] = sum(values) / len(values) if values else 0.0

    return final_scores


# ==============================
# Main
# ==============================

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    k_values = [5, 10]

    qrels_path = "evaluation/qrels.json"
    runs_dir = "evaluation/runs"

    qrels = load_json(qrels_path)

    systems = {}

    for filename in os.listdir(runs_dir):
        if filename.endswith(".json"):
            system_name = filename.replace(".json", "")
            run_path = os.path.join(runs_dir, filename)
            systems[system_name] = load_json(run_path)

    print("=" * 60)
    print("Evaluation Results")
    print("=" * 60)

    for system_name, run in systems.items():
        scores = evaluate_system(run, qrels, k_values)

        print(f"\nSystem: {system_name}")
        for metric, value in sorted(scores.items()):
            print(f"{metric:10s}: {value:.4f}")


if __name__ == "__main__":
    main()