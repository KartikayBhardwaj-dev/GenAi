# ---------- RETRIEVE CHUNKS ----------

def retrieve_chunks(
    vectorstore,
    query,
    k=5
):

    results = vectorstore.similarity_search_with_score(
        query=query,
        k=k
    )

    filtered_results = []

    print("\n========== RETRIEVED CHUNKS ==========\n")

    for i, (doc, score) in enumerate(results):

        print(f"\nCHUNK {i+1}")
        print(f"SCORE: {score}")
        print(doc.page_content[:500])

        # IMPORTANT:
        # Higher threshold = less strict

        if score < 5.0:

            filtered_results.append(
                (doc, score)
            )

    return filtered_results