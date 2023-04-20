using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PortalEnter : MonoBehaviour
{
    public GameObject destinationPortal;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            collision.transform.position = new Vector2 (destinationPortal.transform.position.x, destinationPortal.transform.position.y);
        }
    }
}
