<script>
  async function fetchModels() {
    const response = await fetch('https://huggingface.co/api/models');
    const data = await response.json();

    // Extract relevant model information
    const models = data.map(model => ({
      label: model.modelId,
      value: model.modelId,
      downloads: model.downloads,
      createdAt: new Date(model.createdAt)
    }));

    // Sort models by downloads and createdAt
    const topDownloads = models.sort((a, b) => b.downloads - a.downloads).slice(0, 3);
    const recentUploads = models.sort((a, b) => b.createdAt - a.createdAt).slice(0, 3);

    // Combine and return the final list of models
    return [...topDownloads, ...recentUploads, ...models];
  }

  // Fetch model data and populate the models array
  fetchModels().then(models => {
    $("#model_name").autocomplete({
      source: function(request, response) {
        const results = $.ui.autocomplete.filter(models, request.term);
        response(results.slice(0, 5));
      },
      minLength: 0,
      delay: 200,
      autoFocus: true
    }).on('focus', function() {
      $(this).autocomplete('search', '');
    });
  });
</script>
