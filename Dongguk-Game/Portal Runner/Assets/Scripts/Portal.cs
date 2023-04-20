using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Portal : MonoBehaviour
{
    private Rigidbody2D enteredRigidbody;
    private float enterVelocity, exitVelocity;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        enteredRigidbody = collision.GetComponent<Rigidbody2D>();
        enterVelocity = enteredRigidbody.velocity.x;

        if (gameObject.name == "APortal")
        {
            PortalControl.portalControlInstance.DisableCollider("b");
            PortalControl.portalControlInstance.CreateClone("atB");
        }
        else if (gameObject.name == "BPortal")
        {
            PortalControl.portalControlInstance.DisableCollider("a");
            PortalControl.portalControlInstance.CreateClone("atA");
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        exitVelocity = enteredRigidbody.velocity.x;

        if (enterVelocity != exitVelocity)
        {
            Destroy(GameObject.Find("Clone"));
        }
        else if (gameObject.name != "Clone")
        {
            Destroy(collision.gameObject);
            PortalControl.portalControlInstance.EnableColliders();
            GameObject.Find("Clone").name = "Character";
        }
    }
}
