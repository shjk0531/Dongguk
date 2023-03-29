using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnCollision_Hide : MonoBehaviour
{

    public string targetObjectName;
    public string hideObjectName;

    void Start()
    {
        
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.name == targetObjectName)
        {
            GameObject hideObject = GameObject.Find(hideObjectName);
            hideObject.SetActive(false);
        }
    }
}
