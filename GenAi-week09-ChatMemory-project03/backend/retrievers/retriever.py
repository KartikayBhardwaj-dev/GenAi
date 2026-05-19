def retrieve_chunks(vectorstore, query, k=3):
    results = vectorstore.similarity_search_with_score(query=query, k=k)
    return results
