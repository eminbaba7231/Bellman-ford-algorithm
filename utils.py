# Yardımcı fonksiyonlar - İsteğe bağlı kullanılabilir

def format_step(step):
    return {k: (v if v != float('inf') else "∞") for k, v in step.items()}
