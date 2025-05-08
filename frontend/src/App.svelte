<script>
  // @ts-nocheck
  
    import { onMount } from 'svelte';
    let taches = [];
    let newtache = '';
    let filters ={
      
      etat :'',
    }
    let etatOptions =['à faire','faite' ]
   
  
    const API_URL = 'http://localhost:8000/taches/';
  
    async function fetchtaches() {
      const res = await fetch(API_URL);
      taches = await res.json();
    }
  
    async function Ajouter() {
      if (newtache.trim() === '') return;
      await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tache: newtache, etat: false })
      });
      newtache = '';
      fetchtaches();
    }
    async function Modifier(tache) {
      await fetch(`${API_URL}${tache.id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: tache.id, tache: tache.tache, etat: tache.etat })
      });
      fetchtaches();
    }
  
    async function Supprimer(id) {
      await fetch(`${API_URL}${id}/`, { method: 'DELETE' });
      fetchtaches();
    }
  
    onMount(fetchtaches);
  </script>
  
  <main>
    <h1> Ajouter des Tâches</h1>
    <input type="text" bind:value={newtache} placeholder="Nouvelle tâche" />
    <button on:click={Ajouter}>Ajouter</button>
    <h1>Liste de Tâches</h1>
    <table>
      <thead>
        <tr>
          <th></th>
          <th>Tâche</th>
          <th>
            <select bind:value={filters.etat}>
              <option value=""> état</option>
              {#each etatOptions as option}
                <option value={option}>{option}</option>
              {/each}
            </select>
        </tr>
      </thead>
      <tbody>
        {#each taches.filter(tache => filters.etat === '' || (filters.etat === 'faite' && tache.etat) || (filters.etat === 'à faire' && !tache.etat)) as tache}
        <tr>
            <td>    <input
              type="checkbox"
              checked={tache.etat}
               on:change={() => Modifier({ ...tache, etat: !tache.etat })} />     
  
            </td>
            <td>
              <input  type="text" bind:value={tache.tache} on:change={(e) => Modifier({ ...tache, tache: e.target.value })} />
             </td>
            
            
            
            <td>{tache.etat ? 'faite' : 'à faire' }</td>
  
            <td><button on:click={() => Supprimer(tache.id)}>Supprimer</button>
  
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
    
  
   
  </main>
 
  