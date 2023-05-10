using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomCreatePrefab : MonoBehaviour
{
    public GameObject prefab;
    public float intervalSec = 1;

    private void Start()
    {
        InvokeRepeating("CreatePrefab", 1, intervalSec);
    }

    void CreatePrefab()
    {
        Vector3 area = GetComponent<SpriteRenderer>().bounds.size;

        Vector3 newPos = this.transform.position;
        newPos.x += Random.Range(-area.x / 2, area.x / 2);
        newPos.y += Random.Range(-area.y / 2, 0);
        newPos.z = 5;


        GameObject newGameObject = Instantiate(prefab) as GameObject;
        newGameObject.transform.position = newPos;
    }
}
