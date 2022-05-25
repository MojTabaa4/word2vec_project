import os
import pickle

from django.shortcuts import render
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from .forms import WordForm


def find_most_similar(request):
    similars = []

    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            module_dir = os.path.dirname(__file__)

            cd = form.cleaned_data
            word = cd.get('word')
            num_words = int(cd.get('num_word'))

            load_file_name = 'word_vectors/weights_nneg200_em200_ep50_vocs8921_ws5.npy'
            file_path = os.path.join(module_dir, load_file_name)
            weights = np.load(file_path)
            cosine_matrix = cosine_similarity(weights, weights)

            with open(os.path.join(module_dir, 'word_vectors/id_to_word.pkl'), 'rb') as f:
                id_to_word = pickle.load(f)

            with open(os.path.join(module_dir, 'word_vectors/word_to_id.pkl'), 'rb') as f:
                word_to_id = pickle.load(f)

            try:
                for word_id in cosine_matrix[word_to_id[word]].argsort()[::-1][0:num_words]:
                    similars.append(id_to_word[word_id])
            except:
                similars.append('Word not found')
    form = WordForm()

    return render(
        request,
        'n_similar.html',
        {
            "form": form,
            "similars": similars
        }
    )
